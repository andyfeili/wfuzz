from wfuzz.plugin_api.base import BasePlugin

from wfuzz.externals.moduleman.plugin import moduleman_plugin

@moduleman_plugin
class headers(BasePlugin):
    name = "headers"
    author = ("Xavi Mendez (@xmendez)",)
    version = "0.1"
    summary = "Looks for server headers"
    category = ["default", "passive"]
    priority = 99

    def validate(self, fuzzresult):
	return True

    def process(self, fuzzresult):
        serverh = ""
	poweredby = ""

	if "Server" in fuzzresult.history.headers.response:
	    serverh = fuzzresult.history.headers.response["Server"]

	if "X-Powered-By" in fuzzresult.history.headers.response:
	    poweredby = fuzzresult.history.headers.response["X-Powered-By"]

        if serverh != "":
	    if not self.has_kbase("server"):
		self.add_kbase("server", serverh)
		self.add_result("Server header first set - " + serverh)
	    elif serverh not in self.get_kbase("server"):
		self.add_kbase("server", serverh)
		self.add_result("New Server header - " + serverh)

        if poweredby != "":
	    if not self.has_kbase("poweredby"):
		self.add_kbase("poweredby", poweredby)
		self.add_result("Powered-by header first set - " + poweredby)
	    elif poweredby not in self.get_kbase("poweredby"):
		self.add_kbase("poweredby", poweredby)
		self.add_result("New X-Powered-By header - " + poweredby)
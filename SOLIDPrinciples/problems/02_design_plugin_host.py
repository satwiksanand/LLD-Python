# Task: split LifecyclePlugin into focused lifecycle contracts, keeping PluginHost's behavior identical (Interface Segregation).
# - Keep a small base contract for pluginName().
# - One interface per moment: start (onStart), request (onRequest(path)), stop (onStop).
# - LoggerPlugin implements start + stop, CachePlugin start + request, MetricsPlugin request + stop.
# - Remove the empty-string placeholder hooks.
# - PluginHost fires only the plugins that implement a hook, in install order, and derives
#   hooksFor(index) from the implemented contracts instead of from empty results.
from abc import ABC, abstractmethod

# class LifecyclePlugin(ABC):
#     @abstractmethod
#     def pluginName(self) -> str:
#         ...
#
#     @abstractmethod
#     def onStart(self) -> str:
#         ...
#
#     @abstractmethod
#     def onRequest(self, path: str) -> str:
#         ...
#
#     @abstractmethod
#     def onStop(self) -> str:
#         ...
#
#
# class LoggerPlugin(LifecyclePlugin):
#     def pluginName(self) -> str:
#         return "logger"
#
#     def onStart(self) -> str:
#         return "logger started"
#
#     def onRequest(self, path: str) -> str:
#         return ""
#
#     def onStop(self) -> str:
#         return "logger stopped"
#
#
# class CachePlugin(LifecyclePlugin):
#     def pluginName(self) -> str:
#         return "cache"
#
#     def onStart(self) -> str:
#         return "cache warmed"
#
#     def onRequest(self, path: str) -> str:
#         return "cache checked " + path
#
#     def onStop(self) -> str:
#         return ""
#
#
# class MetricsPlugin(LifecyclePlugin):
#     def pluginName(self) -> str:
#         return "metrics"
#
#     def onStart(self) -> str:
#         return ""
#
#     def onRequest(self, path: str) -> str:
#         return "metrics counted " + path
#
#     def onStop(self) -> str:
#         return "metrics flushed"
#
#
# class PluginHost:
#     def __init__(self):
#         self.plugins: List[LifecyclePlugin] = []
#
#     def _at(self, index: int):
#         if index < 0 or index >= len(self.plugins):
#             return None
#         return self.plugins[index]
#
#     def addLogger(self) -> int:
#         self.plugins.append(LoggerPlugin())
#         return len(self.plugins) - 1
#
#     def addCache(self) -> int:
#         self.plugins.append(CachePlugin())
#         return len(self.plugins) - 1
#
#     def addMetrics(self) -> int:
#         self.plugins.append(MetricsPlugin())
#         return len(self.plugins) - 1
#
#     def pluginCount(self) -> int:
#         return len(self.plugins)
#
#     def pluginName(self, index: int) -> str:
#         plugin = self._at(index)
#         if plugin is None:
#             return "UNKNOWN"
#         return plugin.pluginName()
#
#     def hooksFor(self, index: int) -> str:
#         plugin = self._at(index)
#         if plugin is None:
#             return "UNKNOWN"
#
#         hooks: List[str] = []
#         if plugin.onStart() != "":
#             hooks.append("start")
#         if plugin.onRequest("") != "":
#             hooks.append("request")
#         if plugin.onStop() != "":
#             hooks.append("stop")
#         return ",".join(hooks)
#
#     def fireStart(self) -> List[str]:
#         output: List[str] = []
#         for plugin in self.plugins:
#             result = plugin.onStart()
#             if result != "":
#                 output.append(result)
#         return output
#
#     def fireRequest(self, path: str) -> List[str]:
#         output: List[str] = []
#         for plugin in self.plugins:
#             result = plugin.onRequest(path)
#             if result != "":
#                 output.append(result)
#         return output
#
#     def fireStop(self) -> List[str]:
#         output: List[str] = []
#         for plugin in self.plugins:
#             result = plugin.onStop()
#             if result != "":
#                 output.append(result)
#         return output


# Your PluginHost object will be instantiated and called as such:
# obj = PluginHost()
# param_1 = obj.addLogger()
# param_2 = obj.addCache()
# param_3 = obj.addMetrics()
# param_4 = obj.pluginCount()
# param_5 = obj.pluginName(index)
# param_6 = obj.hooksFor(index)
# param_7 = obj.fireStart()
# param_8 = obj.fireRequest(path)
# param_9 = obj.fireStop()


# Good Example
class LifeCyclePlugin(ABC):
    @abstractmethod
    def pluginName(self) -> str:
        ...

class StartLifecyclePlugin(LifeCyclePlugin):
    @abstractmethod
    def onStart(self) -> str:
        ...

class RequestLifecyclePlugin(LifeCyclePlugin):
    @abstractmethod
    def onRequest(self, path: str) -> str:
        ...

class StopLifecyclePlugin(LifeCyclePlugin):
    @abstractmethod
    def onStop(self) -> str:
        ...

class LoggerPlugin(StartLifecyclePlugin, StopLifecyclePlugin):
    def pluginName(self) -> str:
        return "logger"

    def onStart(self) -> str:
        return "logger started"

    def onStop(self) -> str:
        return "logger stopped"

class CachePlugin(StartLifecyclePlugin, RequestLifecyclePlugin):
    def pluginName(self) -> str:
        return "cache"

    def onStart(self) -> str:
        return "cache warmed"

    def onRequest(self, path: str) -> str:
        return "cache checked " + path

class MetricsPlugin(RequestLifecyclePlugin, StopLifecyclePlugin):
    def pluginName(self) -> str:
        return "metrics"

    def onRequest(self, path: str) -> str:
        return "metrics counted " + path

    def onStop(self) -> str:
        return "metrics flushed"


class PluginHost:
    def __init__(self):
        self.plugins = []

    def _at(self, index: int):
        if index < 0 or index >= len(self.plugins):
            return None
        return self.plugins[index]

    def addLogger(self) -> int:
        self.plugins.append(LoggerPlugin())
        return len(self.plugins) - 1

    def addCache(self) -> int:
        self.plugins.append(CachePlugin())
        return len(self.plugins) - 1

    def addMetrics(self) -> int:
        self.plugins.append(MetricsPlugin())
        return len(self.plugins) - 1

    def pluginCount(self) -> int:
        return len(self.plugins)

    def pluginName(self, index: int) -> str:
        plugin = self._at(index)
        if plugin is None:
            return "UNKNOWN"
        return plugin.pluginName()

    def hooksFor(self, index: int) -> str:
        plugin = self._at(index)
        if plugin is None:
            return "UNKNOWN"

        hooks: List[str] = []
        if isinstance(plugin, StartLifecyclePlugin):
            hooks.append("start")
        if isinstance(plugin, RequestLifecyclePlugin):\
            hooks.append("request")
        if isinstance(plugin, StopLifecyclePlugin):
            hooks.append("stop")

        return ",".join(hooks)

    def fireStart(self) -> List[str]:
        output: List[str] = []
        for plugin in self.plugins:
            if isinstance(plugin, StartLifecyclePlugin):
                output.append(plugin.onStart())
        return output

    def fireRequest(self, path: str) -> List[str]:
        output: List[str] = []
        for plugin in self.plugins:
            if isinstance(plugin, RequestLifecyclePlugin):
                output.append(plugin.onRequest(path))
        return output

    def fireStop(self) -> List[str]:
        output: List[str] = []
        for plugin in self.plugins:
            if isinstance(plugin, StopLifecyclePlugin):
                output.append(plugin.onStop())
        return output
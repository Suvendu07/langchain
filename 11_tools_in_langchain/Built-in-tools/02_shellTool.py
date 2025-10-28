from langchain_community.tools import ShellTool

shell_tool = ShellTool()

result = shell_tool.invoke("who am i")

print(result)
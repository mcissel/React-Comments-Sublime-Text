import sublime, sublime_plugin

class ReactCommentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():

      someUncommented = False
      lines = self.view.lines(region)
      for line in lines:
        if not isCommentLine(self, line):
          someUncommented = True


      if someUncommented:
        for line in reversed(lines):
          if not isCommentLine(self, line):
            addComments(self, edit, line)
      else:
        removeComments(self, edit, self.view.line(region))


def isCommentLine(self, line):
  if "comment.block.js" in self.view.scope_name(line.begin()):
    return True

  lineStr = self.view.substr(line)
  return "{/*" in lineStr or "*/}" in lineStr


def addComments(self, edit, line):
  self.view.insert(edit, line.end(), " */}")
  self.view.insert(edit, line.begin(), "{/* ")


def removeComments(self, edit, region):
  regionStr = self.view.substr(region)
  uncommented = regionStr.replace("{/* ", "").replace(" */}", "")
  self.view.replace(edit, region, uncommented)

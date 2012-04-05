from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def signlist (signlist):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\u59d3\u540d,\u51fa\u751f\u5e74\u6708\u65e5,\u5730\u5740,\u96fb\u8a71\n'])
    for r in loop.setup(signlist):
        extend_([escape_((r.name), True), u',', escape_((r.birth), True), u',', escape_((r.addr), True), u',', escape_((r.phone), True), u'\n'])

    return self

signlist = CompiledTemplate(signlist, 'templates\\signlist.html')
join_ = signlist._join; escape_ = signlist._escape

# coding: utf-8
def summary (signlist):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE HTML>\n'])
    extend_([u'<html>\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>\u9023\u7f72\u8cc7\u6599</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body id="home">\n'])
    extend_([u'    <ul>\n'])
    for r in loop.setup(signlist):
        extend_(['        ', u'<li><a href="', escape_((r.url), True), u'">', escape_((r.text), True), u'</a></li>\n'])
    extend_([u'    </ul>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

summary = CompiledTemplate(summary, 'templates\\summary.html')
join_ = summary._join; escape_ = summary._escape

# coding: utf-8
def thanks (name):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE HTML>\n'])
    extend_([u'<html>\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>\u611f\u8b1d\u60a8\u7684\u9023\u7f72</title>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body id="home">\n'])
    extend_([u'    <div>\u611f\u8b1d\u60a8\u7684\u9023\u7f72</div> \n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

thanks = CompiledTemplate(thanks, 'templates\\thanks.html')
join_ = thanks._join; escape_ = thanks._escape


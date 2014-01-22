serpentPOS
==========
serpentPOS is a python port of <a href="http://code.google.com/p/jspos/">jspos</a>. In other words, this is not my work.

Usage:

    >>> import lexer
    >>> import postagger
    >>> string = 'This is some text to be tagged by the tagger'
  
    >>> words = lexer.Lexer().lex(string)
    >>> print postagger.POSTagger().tag(words)
    [('This', u'DT'), ('is', u'VBZ'), ('some', u'DT'), ('text', u'NN'), ('to', u'TO'), ('be', u'VB'), ('tagged', u'VBN'),
    ('by', u'IN'), ('the', u'DT'), ('tagger', u'NN')]

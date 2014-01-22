serpentPOS
==========
serpentPOS is a python port of <a href="http://code.google.com/p/jspos/">jspos</a> and is **_not_** my work.
I needed it so I figured I'd share the code.

Usage:

    >>> from serpentPOS import lexer, postagger
    >>> string = 'This is some text to be tagged by the tagger'
  
    >>> words = lexer.Lexer().lex(string)
    >>> print postagger.POSTagger().tag(words)
    [('This', u'DT'), ('is', u'VBZ'), ('some', u'DT'), ('text', u'NN'), ('to', u'TO'), ('be', u'VB'), ('tagged', u'VBN'),
    ('by', u'IN'), ('the', u'DT'), ('tagger', u'NN')]

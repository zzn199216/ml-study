import graphlab
products = graphlab.SFrame('amazon_baby.gl/')
products.head()
products['word_count'] = graphlab.text_analytics.count_words(products['review'])
products.head()
graphlab.canvas.set_target('ipynb')
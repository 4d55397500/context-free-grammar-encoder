# context-free-grammar-encoder

Encodes statements from a context-free grammar into a one-hot vector representation based on a pre-order traversal of the parse tree. Specifically, for any given statement, a sequence of one hot vectors are generated ordered according to pre-order tree traversal, with the one-hot index for that vector being the index of the grammar production at the corresponding node of the parse tree.

This allows neural networks to capitalize off the grammar structure, for example in https://arxiv.org/abs/1703.01925

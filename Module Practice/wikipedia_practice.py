# Wikipedia is a multilingual online encyclopedia created and maintained as an open collaboration project by a
# community of volunteer editors using a wiki-based editing system.
# wikipedia is a python library that makes it easy to access and parse data from Wikipedia.
# Installation: pip install wikipedia
# Further more information available on API documentation.

import wikipedia

result = wikipedia.summary("Bangladesh", 10)
carry_propagation = wikipedia.summary("carry propagation", 10)  # Can't give proper result.
print(carry_propagation)

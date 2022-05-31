from stegano import lsbset
from stegano.lsbset import generators

secret_message = "All your"
secret_image = lsbset.hide("./100KB.jpg", secret_message, generators.eratosthenes())
secret_image.save("./100KB.jpg")

secret_message = "base are belong"
secret_image = lsbset.hide("./1MB.jpg", secret_message, generators.eratosthenes())
secret_image.save("./1MB.jpg")

secret_message = "to us."
secret_image = lsbset.hide("./10MB.jpg", secret_message, generators.eratosthenes())
secret_image.save("./10MB.jpg")

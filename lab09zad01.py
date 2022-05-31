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

"""
from stegano import lsb

secret = lsb.hide("./test/100KB.png", "All your")
secret.save("./100KB.png")
print(lsb.reveal("./100KB.png"))

secret = lsb.hide("./test/1MB.png", "base are belong")
secret.save("./1MB.png")
print(lsb.reveal("./1MB.png"))

secret = lsb.hide("./test/10MB.png", "to us.")
secret.save("./10MB.png")
print(lsb.reveal("./10MB.png"))
"""

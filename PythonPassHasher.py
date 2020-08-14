import time
import bcrypt

# When using any of the Bcrypt functions, must use Byte Stings.
password = b"ThisIsMyHiddenPassword500"

hashedPass = bcrypt.hashpw(password, bcrypt.gensalt())

print(hashedPass)


# Here is the first Hash cycle on the Password:- b'$2b$12$a1SmtWr6qcOqPpNcXtUFWezmRw3sy73KaKyKvz2K7zpM7C.oaap66'
# Second Hash run:- b'$2b$12$StT9OHr1Z2Oe53n6Z7U9j.WmLTh8WhkbmI.to.kFye/xZWTpYnRJe'
# Third Hash run:- b'$2b$12$NaIUczPwiYt9jIYTqPfsXOoAj8EiFdQy.fVEXR7n72vPETbvFSVay'
# These are 3 different hashes of the exact same Password:- b"ThisIsMyHiddenPassword500"

# Checking a PlainText Password against a stored Hash.

# In my example here the password variable matches the hashedPass.
if bcrypt.checkpw(password, hashedPass):
    print("The Password Hash matches the PlainText Password!")
else:
    print("The Password Hash does NOT match the PlainText Password!")


# The Workfactor in Bcrypt is the effort/time it takes to hash a desired password.


password2 = b"Password222"
hashedPass2 = bcrypt.hashpw(password2, bcrypt.gensalt())

start = time.time()
hashedPass2 = bcrypt.hashpw(password2, bcrypt.gensalt())
end = time.time()

f = end - start
print(f)

# This section of code will hash the password2 variable and then print the amout of time it took to do so.

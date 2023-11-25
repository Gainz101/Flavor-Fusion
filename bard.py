from bardapi import Bard

# Replace API_KEY with your actual API key
API_KEY = "dQjZqQzR9M6HH_KhYMoag7vDze3qTkG_nizXGID8HuRPEU2IqX-bXks9SqlB1DMnzGaudA."

bard = Bard(token=API_KEY)

result = bard.get_answer("What is the capital of France?")
print(result)

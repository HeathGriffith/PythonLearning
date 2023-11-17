'''For (A), replace the positional arguments in the following code with keyword arguments, which can be passed in any order:

import boto3

def translate_text(text, source_language_code, target_language_code): 
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, 
        SourceLanguageCode=source_language_code, 
        TargetLanguageCode=target_language_code
    )
    print(response) 

def main():
    translate_text('I am learning to code in AWS','en','fr')

if __name__=="__main__":
    main()
'''

'''(A)
import boto3

def translate_text(**kwargs): # replaced positional arguments with **kwargs
    client = boto3.client('translate')
    response = client.translate_text(**kwargs) #removed all parameters and replaced with **kwargs
    print(response) 

def main(): # define keyword arguments in the function call
    translate_text(Text='I am learning to code in AWS',SourceLanguageCode='en',TargetLanguageCode='fr')

if __name__=="__main__":
    main()
    '''

'''For (B), AWS often returns info in the dictionary `"key":"value"` format, and we can use these as our keyword values.

(B)'''
import boto3

def translate_text(**kwargs): # ** is used to indicate that the function accepts any number of keyword arguments
    client = boto3.client('translate')
    response = client.translate_text(**kwargs) # **kwargs is used to collect all keyword arguments in a dictionary
    print(response) 

kwargs={ # defined a variable called "kwargs" (convention) and assigned it a dictionary and placed each key-value pair on a separate line for readability
    "Text":"I am learning to code in AWS",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
    }

def main():# Calls the translate_text function, and the '**' unpacks the 'kwargs' dictionary into keyword arguments
    translate_text(**kwargs)


if __name__=="__main__":
    main()

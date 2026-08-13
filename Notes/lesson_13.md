## Dictionaries -- Another type to store multiple data in Key:Value concept.

dictionary[key] = value

# It uses curly braces.

## Syntax:
  variable_name = {"Key":"Value",
              "Key":"Value",}

## To Accessing values we use the concept of "Key"
       print(variable_name["Key"])

## Adding value :
       variable_name["Key"]= "New_value'

### 
for i in variable_name()  ---> Return Key
for i in variable_name().value() --> return value based on Key
for i in variable_name().item()  --> return both key and value

## dictionary["outer_key"]["inner_key"]

## for outer_key, inner_dict in dictionary.items():
    print(inner_dict["some_key"])

## Nested Dictionaries:
    outer_dictionary =
    {
       "inner_dic_1" : 
       {
            "Key" : "Value",
            "Key" : "Value"
       },
       "inner_dic_2" : 
       {
            "Key" : "Value",
            "Key" : "Value"
       }
    }

## update()
Normal Dictionaries
dic.update({ 
       "Key" : "Value",
       "Key" : "Value"
  })

Nested Dictionaries
  outer_dic["inner_dic"].update({ 
       "Key" : "Value",
       "Key" : "Value"
  })

# setdefault()
dic.setdefault("Key": "value")
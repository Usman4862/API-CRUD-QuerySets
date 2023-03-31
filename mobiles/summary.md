# Custom Permissions

## I have added Custom Permissions by making new dir of `custompermissions.py` in which i use has_permission and has_object_permission methods to authorize users for different methods. this is awesome to use for the authorization to the user as your desire

## In my `custompermissions.py` i write my custom class `MyPermission` in which i am inheriting `BasePermission` and use different methods to allow users for the authorization. After it, i have used this custom permission class in the `permissions_class` . 
from rest_framework import generics
from rest_framework.views import APIView


class MethodPermissionCheckAPIView(APIView):
    """
    Adds extra methods to the ``GenericAPIView`` class to handle the getting and checking of method permissons.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        method = self.request.method.lower()

        try:
            use_permission_classes = getattr(self, '%s_permission_classes' % method)
        except AttributeError:
            use_permission_classes = self.permission_classes

        return [permission() for permission in use_permission_classes]


class CreateAPIView(generics.CreateAPIView, MethodPermissionCheckAPIView):
    """
    View for creating objects. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class ListAPIView(generics.ListAPIView, MethodPermissionCheckAPIView):
    """
    View for listing objects. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class RetrieveAPIView(generics.RetrieveAPIView, MethodPermissionCheckAPIView):
    """
    View for getting an object. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class UpdateAPIView(generics.UpdateAPIView, MethodPermissionCheckAPIView):
    """
    View for updating an object. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class DestroyAPIView(generics.DestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for deleting an object. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """


class ListCreateAPIView(generics.ListCreateAPIView, MethodPermissionCheckAPIView):
    """
    View for listing objects or creating an object. It also implements the MethodPermissionCheckAPIView to allow for
    finer grained method permission checking.
    """


class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for getting, updating or deleting an object. It also implements the MethodPermissionCheckAPIView to allow for
    finer grained method permission checking.
    """


class RetrieveUpdateAPIView(generics.RetrieveAPIView, generics.UpdateAPIView, MethodPermissionCheckAPIView):
    """
    View for getting or updating an object. It also implements the MethodPermissionCheckAPIView to allow for finer
    grained method permission checking.
    """


class RetrieveDestroyAPIView(generics.RetrieveAPIView, generics.DestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for getting or deleting an object. It also implements the MethodPermissionCheckAPIView to allow for finer
    grained method permission checking.
    """


class UpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView, MethodPermissionCheckAPIView):
    """
    View for updating or deleting an object. It also implements the MethodPermissionCheckAPIView to allow for finer
    grained method permission checking.
    """

class MongoCreateAPIView(CreateAPIView, MethodPermissionCheckAPIView):
    """
    View for creating objects. It also implements the MethodPermissionCheckAPIView to allow for finer grained method
    permission checking.
    """



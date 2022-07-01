from rest_framework import viewsets, mixins


class FollowViewSetBase(viewsets.GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin):
    pass

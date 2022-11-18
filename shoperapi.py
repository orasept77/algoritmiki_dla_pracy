# -*- coding: utf-8 -*-


class ShoperWrapper(object):
    """Simple wrapper around Shoper REST API - handles CRUD operations and pagination

    :param shoper_client: Shoper client
    :type shoper_client: :mod:`shoperapi.ShoperClient`
    :param resource: Name of Shoper REST API Resource to use
    :return: The JSON response from API or error
    :rtype: :py:class:`dict` or :py:data:`none`
    """

    def __init__(self, shoper_client, resource):
        self._client = shoper_client
        self.resource = resource

    def single(self, resource_id        ):
        return self._client._get(self.resource, params={'id': resource_id})

    def page(self, limit=None, order=None, page=None, offset=None, filters=None):
        return self._client._get(
            self.resource,
            params={
                'limit': limit,
                'order': order,
                'page': page,
                'offset': offset,
                'filters': filters
            }
        )

    def all(self, limit=None, order=None, offset=0, filters=None):
        res = self._client._get(
            self.resource,
            params={
                'limit': limit,
                'order': order,
                'filters': filters
            }
        )

        all_pages = res.get('pages')

        for i in range(offset, all_pages):
            yield self._client._get(
                self.resource,
                params={
                    'limit': limit,
                    'order': order,
                    'page': i+1,
                    'filters': filters
                }
            )

    def update(self, resource_id, data=None):
        return self._client._put(self.resource, params={'id': resource_id}, data=data)

    def insert(self, data=None):
        return self._client._post(self.resource, data=data)

    def delete(self, resource_id):
        return self._client._delete(self.resource, params={'id': resource_id})



if __name__ == "__main__":
    print("Use as module!")

app.factory('UploadSubtitleApi',['ApiService', function(ApiService) {
    var resource = ApiService.createResource( '/api/subtitle/:id');

    return resource;
}]);

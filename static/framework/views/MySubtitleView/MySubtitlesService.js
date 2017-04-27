app.service('MySubtitlesService', ['ApiService','UploadSubtitleApi',
function (ApiService,UploadSubtitleApi) {
    var self = this;

    var init = function(){
        self.lastTenUploads = null;
    };

    this.getObjects = function ( hard_retfresh){
        if (!self.lastTenUploads||hard_retfresh){
            self.lastTenUploads = UploadSubtitleApi.query(function () {
        });
        }
        return self.lastTenUploads;
    };



}]);

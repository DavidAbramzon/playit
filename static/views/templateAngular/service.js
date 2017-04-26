/**
 * Created by ronlv on 26/04/17.
 */
app.service('ManageWordsService', ['ApiService', 'ManageWordsApi',
    function (ApiService, ManageWordsApi) {
        var self = this;

        var init = function () {
            self.userWords = null;
        };

        this.getObjects = function (hard_refresh) {
            if (!self.userWords || hard_refresh) {
                self.userWords = ManageWordsApi.query(function () {
                });
            }
            return self.userWords;
        };


    }]);

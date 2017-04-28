app.service('ApiService', ['$http', '$q', '$location', '$rootScope', function ($http, $q, $location,  $rootScope) {

    var self = this;
    self.user_token = null;
    self.keep_me = true;
    self.refresh_timeout = null;
    var endpoint_path = '/api';

    var init = function () {
    };



    this.ApiRequest = function (url, method, params, data, token, silent_msg) {
        silent_msg = silent_msg ? silent_msg : false;
        var deferred = $q.defer();
        var http_params = {
            method: method,
            url: endpoint_path + url,
            params: params,
            data: data,
            headers: {},
            withCredential: true
        };
        if (token) {
            http_params.headers.Authorization = 'Token ' + token;
        }
        else {
            if (self.user_token) {
                http_params.headers.Authorization = 'Token ' + self.user_token;
            }
        }

        $http(http_params).then(function successCallback(response) {
            if (!silent_msg) {

                self.handleMsg(response, 'suc');
            }

            deferred.resolve(response.data)

        }, function errorCallback(err) {

            if (err.status == 401 && url != 'auth/login') {
                var current_path = $location.path();
                $location.url('/login?redirect=' + current_path);
                self.storeToken(null);
                $rootScope.checkUserAuthenticated();
                $rootScope.loadGlobalUserInfo();
            } else {
                if (err.status == 404) {
                    $rootScope.notFound = true;
                    $rootScope.show_sub_loader = false;
                }
                else {
                    if (!silent_msg) {
                        self.handleMsg(err, 'err');
                    }
                }
            }
            deferred.reject(err)
        });
        return deferred.promise
    };

    this.handleMsg = function (err_obj, type) {
        var err_data = err_obj.data;
        var msg = '';
        if (err_data && err_data.errors) {
            for (var field in err_data.errors) {
                msg += err_data.errors[field][0] + '\n'
            }
        } else {
            if (err_data && err_data.message) {
                msg = err_data.message
            }
            else {
                if (type == 'err' && err_data.message != null) {

                    msg = 'UNEXCPECTED ERROR';
                }
            }
        }
        if (msg) {

            $rootScope.showMsg($rootScope.createMsgObject(msg, type));
        }
    };

    this.createResource = function (apiUrl,paramDefaults,actions){
        paramDefaults = paramDefaults? paramDefaults:null;
        actions = actions? actions:null;
        return $resource('/api/subtitle/:id',paramDefaults,actions);
    };

    init();

}]);
app.controller('ShowQuestionController', ['$stateParams','$timeout', '$scope', 'ApiService', '$location', '$localStorage', '$sessionStorage',
    function ($stateParams, $timeout,$scope, ApiService, $location, $localStorage, $sessionStorage) {
        var apiRequest = ApiService.ApiRequest;

        $scope.gameId = sessionStorage.getItem("gameId");
        apiRequest('/get_next_question/', 'GET', "",
                 "", "", "").then(function (data) {
            $scope.face = data.face;
        });
        $timeout(nextRound, 15000);
        function nextRound() {
            $location.path('/round-summary');
        };
        var _video = null, patData = null;

        $scope.patOpts = {x: 0, y: 0, w: 250, h: 250};

        // Setup a channel to receive a video property
        // with a reference to the video element
        // See the HTML binding in main.html
        $scope.channel = {};

        $scope.webcamError = false;
        $scope.onError = function (err) {
            $scope.$apply(
                function () {
                    $scope.webcamError = err;
                }
            );
        };

        $scope.onSuccess = function () {
            // The video element contains the captured camera data
                _video = $scope.channel.video;
                console.log(_video.height);
                $scope.patOpts.w = _video.width;
                $scope.patOpts.h = _video.height;
                //$scope.showDemos = true;
        };

        $scope.onStream = function (stream) {
            // You could do something manually with the stream.
        };

        $scope.makeSnapshot = function () {
            if (_video) {
                var patCanvas = document.querySelector('#snapshot');
                if (!patCanvas) return;

                patCanvas.width = _video.width;
                patCanvas.height = _video.height;
                var ctxPat = patCanvas.getContext('2d');

                var idata = getVideoData($scope.patOpts.x, $scope.patOpts.y, $scope.patOpts.w, $scope.patOpts.h);
                console.log($scope.patOpts.h);
                ctxPat.putImageData(idata, 0, 0);

                sendSnapshotToServer(patCanvas.toDataURL());

                patData = idata;
            }
        };

        /**
         * Redirect the browser to the URL given.
         * Used to download the image by passing a dataURL string
         */
        $scope.downloadSnapshot = function downloadSnapshot(dataURL) {
            window.location.href = dataURL;
        };

        var getVideoData = function getVideoData(x, y, w, h) {
            var hiddenCanvas = document.createElement('canvas');
            // hiddenCanvas.width = _video.width;
            // hiddenCanvas.height = _video.height;
            var ctx = hiddenCanvas.getContext('2d');
            ctx.drawImage(_video, 0, 0, hiddenCanvas.width, hiddenCanvas.height);
            return ctx.getImageData(x, y, w, h);
        };

        // (function tick() {
        //     apiRequest('/get_countdown/', 'GET', "",
        //         "", "", "").then(function (data) {
        //         $scope.countDown = data;
        //         if ($scope.countDown > 0) {
        //             $timeout(tick, 1000);
        //         }
        //         else {
        //             //TODO: route to round-summary-view
        //         }
        //
        //     })
        // })();

        /**
         * This function could be used to send the image data
         * to a backend server that expects base64 encoded images.
         *
         * In this example, we simply store it in the scope for display.
         */
        var sendSnapshotToServer = function sendSnapshotToServer(imgBase64) {
            $scope.snapshotData = imgBase64;
            var fd = new FormData();
            fd.append('file', imgBase64);
            apiRequest('/save_answer/', 'POST', "",
                {"answer":imgBase64} , "","", "").then(function (data) {
                $scope.countDown = data;
                if ($scope.countDown > 0) {
                    $timeout(tick, 1000);
                }
            });
        };
    }]);

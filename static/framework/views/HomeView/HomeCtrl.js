'use strict';
/** 
  * Upload subtitle controller
*/
app.controller('HomeCtrl', ['$scope',
function ($scope) {
    var init = function(){
        $scope.lastTenUploads = MySubtitlesService.getObjects();
        console.log("test");
        $scope.open('lg');
    }


    // FILTERS


    // View
    $scope.downloadSubtitle = function (){
    };

    $scope.open = function(size) {

		var modalInstance = $uibModal.open({
			templateUrl : '/static/views/CreationProcessView/creation-process-modal.html',
			controller : 'CreationProcessCtrl',
			size : size,
			resolve : {
				items : function() {
					return $scope.items;
				}
			}
		});

		modalInstance.result.then(function(selectedItem) {
			$scope.selected = selectedItem;
		}, function() {
			$log.info('Modal dismissed at: ' + new Date());
		});
	};


    // CALLBACKS



    init();
}]);
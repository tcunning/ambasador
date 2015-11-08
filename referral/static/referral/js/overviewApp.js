var overviewApp = angular.module('overviewApp', []);

// Allow Django to use {{ xyz }} variables and a
// Allow angular to use {[{ xyz }]} variables 
overviewApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});
 


overviewApp.controller('ReferralListController', ['$scope', '$window', '$http', '$interval', function($scope, $window, $http, $interval) {
    var referralList = this;

    $scope.sortType     = 'name'; // set the default sort type
    $scope.sortReverse  = false;  // set the default sort order
    
    // Currently we disable the local cache and setup a quick timer to
    // refresh our data.
    referralList.referrals = [];  // $window.initialReferrals;
    
    referralList.addReferral = function() {
        var referral = {name:referralList.referralText, count:0};
        
        $http.post("/referral/?format=json", referral)
        .success(function (data, status, headers, config) {
            referralList.referrals.push(referral);
            referralList.referralText = '';
        })
        .error(function (data, status, header, config) {
            alert("Unable to add referral, make sure its name is unique!");
        });       
    };

    referralList.removeReferral = function(referral) {
        $http.delete("/referral/" + referral.name + "/?format=json")
        .success(function (data, status, headers, config) {
            var referralIndex = referralList.referrals.indexOf(referral)
            referralList.referrals.splice(referralIndex,1)
        })
        .error(function (data, status, header, config) {
            alert("Unable to delete data!");
        });       
    };

    referralList.editReferral = function(referral) {
        var replacementReferral = {name:referralList.editName, count:referralList.editCount};
        $http.put("/referral/" + referral.name + "/?format=json", replacementReferral)
        .success(function (data, status, headers, config) {
            var referralIndex = referralList.referrals.indexOf(referral)
            referral.name = referralList.editName
            referral.count = referralList.editCount
            referralList.editName = ''
            referralList.editCount = ''
        })
        .error(function (data, status, header, config) {
            alert("Unable to edit data!");
        });       
    };

    referralList.refresh = function() {
        $http.get('/referral/?format=json', {headers:{'Cache-Control':'no-cache'}, cache:false})
        .success(function (data, status, headers, config) {
            referralList.referrals = data;
        })
        .error(function (data, status, header, config) {
            alert("Unable to refresh data!");
        });
    };
    
    referralList.refresh();
    
}]);


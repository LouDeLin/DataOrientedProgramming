


class UserManagement:
    
    @staticmethod
    def isLibrarian(userManagementData, userId):
        # will be implemented later <2>
        pass
    
    @staticmethod
    def isSuperMember(userManagementData, userId):
        # will be implemented later <2>
        pass


class Catalog:

    @staticmethod
    def getBookLendings(catalogData, memberId):
        # will be implemented later <3>
        pass


class Library:

    # # This is OOP style.
    __catalog = {}
    __userManagement = {}
    def getBookLendings(self, userID, memberID):
        # accesses library state via sef.__catalog and self.__userManagement
        pass

    @staticmethod
    def getBookLendings(libraryData, userId, memberId) :
        if(UserManagement.isLibrarian(libraryData.userManagement, userId) or
           UserManagement.isSuperMember(libraryData.userManagement, userId)):
            return Catalog.getBookLendings(libraryData.catalog, memberId)
        else:
            raise Exception("Not allowed to add a book item") 




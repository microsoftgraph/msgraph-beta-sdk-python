from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user_set = lazy_import('msgraph.generated.models.user_set')

class RequestorSettings(AdditionalDataHolder, Parsable):
    @property
    def accept_requests(self,) -> Optional[bool]:
        """
        Gets the acceptRequests property value. Indicates whether new requests are accepted on this policy.
        Returns: Optional[bool]
        """
        return self._accept_requests
    
    @accept_requests.setter
    def accept_requests(self,value: Optional[bool] = None) -> None:
        """
        Sets the acceptRequests property value. Indicates whether new requests are accepted on this policy.
        Args:
            value: Value to set for the acceptRequests property.
        """
        self._accept_requests = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allowed_requestors(self,) -> Optional[List[user_set.UserSet]]:
        """
        Gets the allowedRequestors property value. The users who are allowed to request on this policy, which can be singleUser, groupMembers, and connectedOrganizationMembers.
        Returns: Optional[List[user_set.UserSet]]
        """
        return self._allowed_requestors
    
    @allowed_requestors.setter
    def allowed_requestors(self,value: Optional[List[user_set.UserSet]] = None) -> None:
        """
        Sets the allowedRequestors property value. The users who are allowed to request on this policy, which can be singleUser, groupMembers, and connectedOrganizationMembers.
        Args:
            value: Value to set for the allowedRequestors property.
        """
        self._allowed_requestors = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new requestorSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether new requests are accepted on this policy.
        self._accept_requests: Optional[bool] = None
        # The users who are allowed to request on this policy, which can be singleUser, groupMembers, and connectedOrganizationMembers.
        self._allowed_requestors: Optional[List[user_set.UserSet]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Who can request. One of NoSubjects, SpecificDirectorySubjects, SpecificConnectedOrganizationSubjects, AllConfiguredConnectedOrganizationSubjects, AllExistingConnectedOrganizationSubjects, AllExistingDirectoryMemberUsers, AllExistingDirectorySubjects or AllExternalSubjects.
        self._scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RequestorSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RequestorSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RequestorSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accept_requests": lambda n : setattr(self, 'accept_requests', n.get_bool_value()),
            "allowed_requestors": lambda n : setattr(self, 'allowed_requestors', n.get_collection_of_object_values(user_set.UserSet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope_type": lambda n : setattr(self, 'scope_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def scope_type(self,) -> Optional[str]:
        """
        Gets the scopeType property value. Who can request. One of NoSubjects, SpecificDirectorySubjects, SpecificConnectedOrganizationSubjects, AllConfiguredConnectedOrganizationSubjects, AllExistingConnectedOrganizationSubjects, AllExistingDirectoryMemberUsers, AllExistingDirectorySubjects or AllExternalSubjects.
        Returns: Optional[str]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeType property value. Who can request. One of NoSubjects, SpecificDirectorySubjects, SpecificConnectedOrganizationSubjects, AllConfiguredConnectedOrganizationSubjects, AllExistingConnectedOrganizationSubjects, AllExistingDirectoryMemberUsers, AllExistingDirectorySubjects or AllExternalSubjects.
        Args:
            value: Value to set for the scopeType property.
        """
        self._scope_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("acceptRequests", self.accept_requests)
        writer.write_collection_of_object_values("allowedRequestors", self.allowed_requestors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("scopeType", self.scope_type)
        writer.write_additional_data_value(self.additional_data)
    


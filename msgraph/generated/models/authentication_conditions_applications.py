from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_condition_application = lazy_import('msgraph.generated.models.authentication_condition_application')

class AuthenticationConditionsApplications(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationConditionsApplications and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The includeAllApplications property
        self._include_all_applications: Optional[bool] = None
        # The includeApplications property
        self._include_applications: Optional[List[authentication_condition_application.AuthenticationConditionApplication]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationConditionsApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationConditionsApplications
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationConditionsApplications()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "include_all_applications": lambda n : setattr(self, 'include_all_applications', n.get_bool_value()),
            "include_applications": lambda n : setattr(self, 'include_applications', n.get_collection_of_object_values(authentication_condition_application.AuthenticationConditionApplication)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def include_all_applications(self,) -> Optional[bool]:
        """
        Gets the includeAllApplications property value. The includeAllApplications property
        Returns: Optional[bool]
        """
        return self._include_all_applications
    
    @include_all_applications.setter
    def include_all_applications(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeAllApplications property value. The includeAllApplications property
        Args:
            value: Value to set for the includeAllApplications property.
        """
        self._include_all_applications = value
    
    @property
    def include_applications(self,) -> Optional[List[authentication_condition_application.AuthenticationConditionApplication]]:
        """
        Gets the includeApplications property value. The includeApplications property
        Returns: Optional[List[authentication_condition_application.AuthenticationConditionApplication]]
        """
        return self._include_applications
    
    @include_applications.setter
    def include_applications(self,value: Optional[List[authentication_condition_application.AuthenticationConditionApplication]] = None) -> None:
        """
        Sets the includeApplications property value. The includeApplications property
        Args:
            value: Value to set for the includeApplications property.
        """
        self._include_applications = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("includeAllApplications", self.include_all_applications)
        writer.write_collection_of_object_values("includeApplications", self.include_applications)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


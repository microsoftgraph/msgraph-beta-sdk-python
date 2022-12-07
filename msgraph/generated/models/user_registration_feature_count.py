from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_feature = lazy_import('msgraph.generated.models.authentication_method_feature')

class UserRegistrationFeatureCount(AdditionalDataHolder, Parsable):
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
        Instantiates a new userRegistrationFeatureCount and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The feature property
        self._feature: Optional[authentication_method_feature.AuthenticationMethodFeature] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of users.
        self._user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserRegistrationFeatureCount:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationFeatureCount
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserRegistrationFeatureCount()
    
    @property
    def feature(self,) -> Optional[authentication_method_feature.AuthenticationMethodFeature]:
        """
        Gets the feature property value. The feature property
        Returns: Optional[authentication_method_feature.AuthenticationMethodFeature]
        """
        return self._feature
    
    @feature.setter
    def feature(self,value: Optional[authentication_method_feature.AuthenticationMethodFeature] = None) -> None:
        """
        Sets the feature property value. The feature property
        Args:
            value: Value to set for the feature property.
        """
        self._feature = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(authentication_method_feature.AuthenticationMethodFeature)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user_count": lambda n : setattr(self, 'user_count', n.get_int_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("feature", self.feature)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_count(self,) -> Optional[int]:
        """
        Gets the userCount property value. Number of users.
        Returns: Optional[int]
        """
        return self._user_count
    
    @user_count.setter
    def user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the userCount property value. Number of users.
        Args:
            value: Value to set for the userCount property.
        """
        self._user_count = value
    


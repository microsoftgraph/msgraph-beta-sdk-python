from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

password_single_sign_on_field = lazy_import('msgraph.generated.models.password_single_sign_on_field')

class PasswordSingleSignOnSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new passwordSingleSignOnSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fields property
        self._fields: Optional[List[password_single_sign_on_field.PasswordSingleSignOnField]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PasswordSingleSignOnSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PasswordSingleSignOnSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PasswordSingleSignOnSettings()
    
    @property
    def fields(self,) -> Optional[List[password_single_sign_on_field.PasswordSingleSignOnField]]:
        """
        Gets the fields property value. The fields property
        Returns: Optional[List[password_single_sign_on_field.PasswordSingleSignOnField]]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[List[password_single_sign_on_field.PasswordSingleSignOnField]] = None) -> None:
        """
        Sets the fields property value. The fields property
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(password_single_sign_on_field.PasswordSingleSignOnField)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


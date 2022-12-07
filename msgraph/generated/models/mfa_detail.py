from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MfaDetail(AdditionalDataHolder, Parsable):
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
    def auth_detail(self,) -> Optional[str]:
        """
        Gets the authDetail property value. Indicates the MFA auth detail for the corresponding Sign-in activity when the MFA Required is 'Yes'.
        Returns: Optional[str]
        """
        return self._auth_detail
    
    @auth_detail.setter
    def auth_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the authDetail property value. Indicates the MFA auth detail for the corresponding Sign-in activity when the MFA Required is 'Yes'.
        Args:
            value: Value to set for the authDetail property.
        """
        self._auth_detail = value
    
    @property
    def auth_method(self,) -> Optional[str]:
        """
        Gets the authMethod property value. Indicates the MFA Auth methods (SMS, Phone, Authenticator App are some of the value) for the corresponding sign-in activity when the MFA Required field is 'Yes'.
        Returns: Optional[str]
        """
        return self._auth_method
    
    @auth_method.setter
    def auth_method(self,value: Optional[str] = None) -> None:
        """
        Sets the authMethod property value. Indicates the MFA Auth methods (SMS, Phone, Authenticator App are some of the value) for the corresponding sign-in activity when the MFA Required field is 'Yes'.
        Args:
            value: Value to set for the authMethod property.
        """
        self._auth_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mfaDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the MFA auth detail for the corresponding Sign-in activity when the MFA Required is 'Yes'.
        self._auth_detail: Optional[str] = None
        # Indicates the MFA Auth methods (SMS, Phone, Authenticator App are some of the value) for the corresponding sign-in activity when the MFA Required field is 'Yes'.
        self._auth_method: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MfaDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MfaDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MfaDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auth_detail": lambda n : setattr(self, 'auth_detail', n.get_str_value()),
            "auth_method": lambda n : setattr(self, 'auth_method', n.get_str_value()),
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
        writer.write_str_value("authDetail", self.auth_detail)
        writer.write_str_value("authMethod", self.auth_method)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


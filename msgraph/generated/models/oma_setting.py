from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class OmaSetting(AdditionalDataHolder, Parsable):
    """
    OMA Settings definition.
    """
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
        Instantiates a new omaSetting and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Description.
        self._description: Optional[str] = None
        # Display Name.
        self._display_name: Optional[str] = None
        # Indicates whether the value field is encrypted. This property is read-only.
        self._is_encrypted: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # OMA.
        self._oma_uri: Optional[str] = None
        # ReferenceId for looking up secret for decryption. This property is read-only.
        self._secret_reference_value_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OmaSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OmaSetting()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display Name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display Name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_encrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oma_uri": lambda n : setattr(self, 'oma_uri', n.get_str_value()),
            "secret_reference_value_id": lambda n : setattr(self, 'secret_reference_value_id', n.get_str_value()),
        }
        return fields
    
    @property
    def is_encrypted(self,) -> Optional[bool]:
        """
        Gets the isEncrypted property value. Indicates whether the value field is encrypted. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_encrypted
    
    @is_encrypted.setter
    def is_encrypted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEncrypted property value. Indicates whether the value field is encrypted. This property is read-only.
        Args:
            value: Value to set for the isEncrypted property.
        """
        self._is_encrypted = value
    
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
    def oma_uri(self,) -> Optional[str]:
        """
        Gets the omaUri property value. OMA.
        Returns: Optional[str]
        """
        return self._oma_uri
    
    @oma_uri.setter
    def oma_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the omaUri property value. OMA.
        Args:
            value: Value to set for the omaUri property.
        """
        self._oma_uri = value
    
    @property
    def secret_reference_value_id(self,) -> Optional[str]:
        """
        Gets the secretReferenceValueId property value. ReferenceId for looking up secret for decryption. This property is read-only.
        Returns: Optional[str]
        """
        return self._secret_reference_value_id
    
    @secret_reference_value_id.setter
    def secret_reference_value_id(self,value: Optional[str] = None) -> None:
        """
        Sets the secretReferenceValueId property value. ReferenceId for looking up secret for decryption. This property is read-only.
        Args:
            value: Value to set for the secretReferenceValueId property.
        """
        self._secret_reference_value_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("omaUri", self.oma_uri)
        writer.write_additional_data_value(self.additional_data)
    


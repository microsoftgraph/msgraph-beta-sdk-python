from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SelfSignedCertificate(AdditionalDataHolder, Parsable):
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
        Instantiates a new SelfSignedCertificate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Custom key identifier.
        self._custom_key_identifier: Optional[bytes] = None
        # The friendly name for the key.
        self._display_name: Optional[str] = None
        # The date and time at which the credential expires. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._end_date_time: Optional[datetime] = None
        # The value for the key credential. Should be a base-64 encoded value.
        self._key: Optional[bytes] = None
        # The unique identifier (GUID) for the key.
        self._key_id: Optional[Guid] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The date and time at which the credential becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._start_date_time: Optional[datetime] = None
        # The thumbprint value for the key.
        self._thumbprint: Optional[str] = None
        # The type of key credential. 'AsymmetricX509Cert'.
        self._type: Optional[str] = None
        # A string that describes the purpose for which the key can be used. For example, 'Verify'.
        self._usage: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SelfSignedCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SelfSignedCertificate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SelfSignedCertificate()
    
    @property
    def custom_key_identifier(self,) -> Optional[bytes]:
        """
        Gets the customKeyIdentifier property value. Custom key identifier.
        Returns: Optional[bytes]
        """
        return self._custom_key_identifier
    
    @custom_key_identifier.setter
    def custom_key_identifier(self,value: Optional[bytes] = None) -> None:
        """
        Sets the customKeyIdentifier property value. Custom key identifier.
        Args:
            value: Value to set for the customKeyIdentifier property.
        """
        self._custom_key_identifier = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The friendly name for the key.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The friendly name for the key.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The date and time at which the credential expires. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The date and time at which the credential expires. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_key_identifier": lambda n : setattr(self, 'custom_key_identifier', n.get_bytes_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "key": lambda n : setattr(self, 'key', n.get_bytes_value()),
            "key_id": lambda n : setattr(self, 'key_id', n.get_object_value(Guid)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "usage": lambda n : setattr(self, 'usage', n.get_str_value()),
        }
        return fields
    
    @property
    def key(self,) -> Optional[bytes]:
        """
        Gets the key property value. The value for the key credential. Should be a base-64 encoded value.
        Returns: Optional[bytes]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[bytes] = None) -> None:
        """
        Sets the key property value. The value for the key credential. Should be a base-64 encoded value.
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
    @property
    def key_id(self,) -> Optional[Guid]:
        """
        Gets the keyId property value. The unique identifier (GUID) for the key.
        Returns: Optional[Guid]
        """
        return self._key_id
    
    @key_id.setter
    def key_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the keyId property value. The unique identifier (GUID) for the key.
        Args:
            value: Value to set for the keyId property.
        """
        self._key_id = value
    
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
        writer.write_object_value("customKeyIdentifier", self.custom_key_identifier)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("key", self.key)
        writer.write_object_value("keyId", self.key_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_str_value("type", self.type)
        writer.write_str_value("usage", self.usage)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time at which the credential becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time at which the credential becomes valid. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def thumbprint(self,) -> Optional[str]:
        """
        Gets the thumbprint property value. The thumbprint value for the key.
        Returns: Optional[str]
        """
        return self._thumbprint
    
    @thumbprint.setter
    def thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbprint property value. The thumbprint value for the key.
        Args:
            value: Value to set for the thumbprint property.
        """
        self._thumbprint = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type of key credential. 'AsymmetricX509Cert'.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type of key credential. 'AsymmetricX509Cert'.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def usage(self,) -> Optional[str]:
        """
        Gets the usage property value. A string that describes the purpose for which the key can be used. For example, 'Verify'.
        Returns: Optional[str]
        """
        return self._usage
    
    @usage.setter
    def usage(self,value: Optional[str] = None) -> None:
        """
        Sets the usage property value. A string that describes the purpose for which the key can be used. For example, 'Verify'.
        Args:
            value: Value to set for the usage property.
        """
        self._usage = value
    


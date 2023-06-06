from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SecurityProviderStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The enabled property
    enabled: Optional[bool] = None
    # The endpoint property
    endpoint: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provider property
    provider: Optional[str] = None
    # The region property
    region: Optional[str] = None
    # The vendor property
    vendor: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecurityProviderStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecurityProviderStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecurityProviderStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "endpoint": lambda n : setattr(self, 'endpoint', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "vendor": lambda n : setattr(self, 'vendor', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("endpoint", self.endpoint)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("region", self.region)
        writer.write_str_value("vendor", self.vendor)
        writer.write_additional_data_value(self.additional_data)
    


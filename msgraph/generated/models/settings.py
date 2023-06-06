from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Settings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies if the user's primary mailbox is hosted in the cloud and is enabled for Microsoft Graph.
    has_graph_mailbox: Optional[bool] = None
    # Specifies if the user has a MyAnalytics license assigned.
    has_license: Optional[bool] = None
    # Specifies if the user opted out of MyAnalytics.
    has_opted_out: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Settings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Settings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Settings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "hasGraphMailbox": lambda n : setattr(self, 'has_graph_mailbox', n.get_bool_value()),
            "hasLicense": lambda n : setattr(self, 'has_license', n.get_bool_value()),
            "hasOptedOut": lambda n : setattr(self, 'has_opted_out', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("hasGraphMailbox", self.has_graph_mailbox)
        writer.write_bool_value("hasLicense", self.has_license)
        writer.write_bool_value("hasOptedOut", self.has_opted_out)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    


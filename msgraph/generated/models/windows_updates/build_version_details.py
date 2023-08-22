from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BuildVersionDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The buildNumber property
    build_number: Optional[int] = None
    # The majorVersion property
    major_version: Optional[int] = None
    # The minorVersion property
    minor_version: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The updateBuildRevision property
    update_build_revision: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BuildVersionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BuildVersionDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BuildVersionDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "buildNumber": lambda n : setattr(self, 'build_number', n.get_int_value()),
            "majorVersion": lambda n : setattr(self, 'major_version', n.get_int_value()),
            "minorVersion": lambda n : setattr(self, 'minor_version', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updateBuildRevision": lambda n : setattr(self, 'update_build_revision', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("buildNumber", self.build_number)
        writer.write_int_value("majorVersion", self.major_version)
        writer.write_int_value("minorVersion", self.minor_version)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("updateBuildRevision", self.update_build_revision)
        writer.write_additional_data_value(self.additional_data)
    


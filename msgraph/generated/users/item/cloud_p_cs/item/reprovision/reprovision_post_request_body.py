from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import cloud_pc_operating_system, cloud_pc_user_account_type

@dataclass
class ReprovisionPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The osVersion property
    os_version: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None
    # The userAccountType property
    user_account_type: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReprovisionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReprovisionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReprovisionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models import cloud_pc_operating_system, cloud_pc_user_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "osVersion": lambda n : setattr(self, 'os_version', n.get_enum_value(cloud_pc_operating_system.CloudPcOperatingSystem)),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(cloud_pc_user_account_type.CloudPcUserAccountType)),
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
        writer.write_enum_value("osVersion", self.os_version)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_additional_data_value(self.additional_data)
    


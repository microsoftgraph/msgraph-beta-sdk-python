from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.group_policy_object_file import GroupPolicyObjectFile

@dataclass
class CreateMigrationReportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The groupPolicyObjectFile property
    group_policy_object_file: Optional[GroupPolicyObjectFile] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateMigrationReportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateMigrationReportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateMigrationReportPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.group_policy_object_file import GroupPolicyObjectFile

        from ....models.group_policy_object_file import GroupPolicyObjectFile

        fields: Dict[str, Callable[[Any], None]] = {
            "groupPolicyObjectFile": lambda n : setattr(self, 'group_policy_object_file', n.get_object_value(GroupPolicyObjectFile)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("groupPolicyObjectFile", self.group_policy_object_file)
        writer.write_additional_data_value(self.additional_data)
    


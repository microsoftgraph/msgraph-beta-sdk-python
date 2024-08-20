from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .advanced_config_state import AdvancedConfigState
    from .exclude_target import ExcludeTarget
    from .include_target import IncludeTarget

@dataclass
class SystemCredentialPreferences(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Users and groups excluded from the preferred authentication method experience of the system.
    exclude_targets: Optional[List[ExcludeTarget]] = None
    # Users and groups included in the preferred authentication method experience of the system.
    include_targets: Optional[List[IncludeTarget]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[AdvancedConfigState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SystemCredentialPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SystemCredentialPreferences
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SystemCredentialPreferences()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .advanced_config_state import AdvancedConfigState
        from .exclude_target import ExcludeTarget
        from .include_target import IncludeTarget

        from .advanced_config_state import AdvancedConfigState
        from .exclude_target import ExcludeTarget
        from .include_target import IncludeTarget

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(ExcludeTarget)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(IncludeTarget)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AdvancedConfigState)),
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
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    


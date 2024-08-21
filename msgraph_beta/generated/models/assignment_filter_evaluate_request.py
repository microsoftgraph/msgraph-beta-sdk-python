from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_platform_type import DevicePlatformType

@dataclass
class AssignmentFilterEvaluateRequest(AdditionalDataHolder, BackedModel, Parsable):
    """
    Request for assignment filter evaluation for devices.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Order the devices should be sorted in. Default is ascending on device name.
    order_by: Optional[List[str]] = None
    # Supported platform types.
    platform: Optional[DevicePlatformType] = None
    # Rule definition of the Assignment Filter.
    rule: Optional[str] = None
    # Search keyword applied to scope found devices.
    search: Optional[str] = None
    # Number of records to skip. Default value is 0
    skip: Optional[int] = None
    # Limit of records per request. Default value is 100, if provided less than 0 or greater than 100
    top: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentFilterEvaluateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterEvaluateRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentFilterEvaluateRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_platform_type import DevicePlatformType

        from .device_platform_type import DevicePlatformType

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orderBy": lambda n : setattr(self, 'order_by', n.get_collection_of_primitive_values(str)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(DevicePlatformType)),
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
            "search": lambda n : setattr(self, 'search', n.get_str_value()),
            "skip": lambda n : setattr(self, 'skip', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("orderBy", self.order_by)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("rule", self.rule)
        writer.write_str_value("search", self.search)
        writer.write_int_value("skip", self.skip)
        writer.write_int_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)
    


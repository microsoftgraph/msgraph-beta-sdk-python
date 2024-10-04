from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_impact_summary import ApplicationImpactSummary
    from .device_impact_summary import DeviceImpactSummary
    from .directory_object_impact_summary import DirectoryObjectImpactSummary
    from .group_impact_summary import GroupImpactSummary
    from .service_principal_impact_summary import ServicePrincipalImpactSummary
    from .user_impact_summary import UserImpactSummary

@dataclass
class ResourceImpactSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The impactedCount property
    impacted_count: Optional[str] = None
    # The impactedCountLimitExceeded property
    impacted_count_limit_exceeded: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceType property
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResourceImpactSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResourceImpactSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.applicationImpactSummary".casefold():
            from .application_impact_summary import ApplicationImpactSummary

            return ApplicationImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.deviceImpactSummary".casefold():
            from .device_impact_summary import DeviceImpactSummary

            return DeviceImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.directoryObjectImpactSummary".casefold():
            from .directory_object_impact_summary import DirectoryObjectImpactSummary

            return DirectoryObjectImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.groupImpactSummary".casefold():
            from .group_impact_summary import GroupImpactSummary

            return GroupImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.servicePrincipalImpactSummary".casefold():
            from .service_principal_impact_summary import ServicePrincipalImpactSummary

            return ServicePrincipalImpactSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.healthMonitoring.userImpactSummary".casefold():
            from .user_impact_summary import UserImpactSummary

            return UserImpactSummary()
        return ResourceImpactSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .application_impact_summary import ApplicationImpactSummary
        from .device_impact_summary import DeviceImpactSummary
        from .directory_object_impact_summary import DirectoryObjectImpactSummary
        from .group_impact_summary import GroupImpactSummary
        from .service_principal_impact_summary import ServicePrincipalImpactSummary
        from .user_impact_summary import UserImpactSummary

        from .application_impact_summary import ApplicationImpactSummary
        from .device_impact_summary import DeviceImpactSummary
        from .directory_object_impact_summary import DirectoryObjectImpactSummary
        from .group_impact_summary import GroupImpactSummary
        from .service_principal_impact_summary import ServicePrincipalImpactSummary
        from .user_impact_summary import UserImpactSummary

        fields: Dict[str, Callable[[Any], None]] = {
            "impactedCount": lambda n : setattr(self, 'impacted_count', n.get_str_value()),
            "impactedCountLimitExceeded": lambda n : setattr(self, 'impacted_count_limit_exceeded', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        writer.write_str_value("impactedCount", self.impacted_count)
        writer.write_bool_value("impactedCountLimitExceeded", self.impacted_count_limit_exceeded)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_additional_data_value(self.additional_data)
    


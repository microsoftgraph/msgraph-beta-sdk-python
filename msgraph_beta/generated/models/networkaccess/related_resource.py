from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .related_destination import RelatedDestination
    from .related_device import RelatedDevice
    from .related_malware import RelatedMalware
    from .related_process import RelatedProcess
    from .related_remote_network import RelatedRemoteNetwork
    from .related_tenant import RelatedTenant
    from .related_threat_intelligence import RelatedThreatIntelligence
    from .related_token import RelatedToken
    from .related_user import RelatedUser
    from .related_web_category import RelatedWebCategory

@dataclass
class RelatedResource(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedDestination".casefold():
            from .related_destination import RelatedDestination

            return RelatedDestination()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedDevice".casefold():
            from .related_device import RelatedDevice

            return RelatedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedMalware".casefold():
            from .related_malware import RelatedMalware

            return RelatedMalware()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedProcess".casefold():
            from .related_process import RelatedProcess

            return RelatedProcess()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedRemoteNetwork".casefold():
            from .related_remote_network import RelatedRemoteNetwork

            return RelatedRemoteNetwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedTenant".casefold():
            from .related_tenant import RelatedTenant

            return RelatedTenant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedThreatIntelligence".casefold():
            from .related_threat_intelligence import RelatedThreatIntelligence

            return RelatedThreatIntelligence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedToken".casefold():
            from .related_token import RelatedToken

            return RelatedToken()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedUser".casefold():
            from .related_user import RelatedUser

            return RelatedUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.networkaccess.relatedWebCategory".casefold():
            from .related_web_category import RelatedWebCategory

            return RelatedWebCategory()
        return RelatedResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .related_destination import RelatedDestination
        from .related_device import RelatedDevice
        from .related_malware import RelatedMalware
        from .related_process import RelatedProcess
        from .related_remote_network import RelatedRemoteNetwork
        from .related_tenant import RelatedTenant
        from .related_threat_intelligence import RelatedThreatIntelligence
        from .related_token import RelatedToken
        from .related_user import RelatedUser
        from .related_web_category import RelatedWebCategory

        from .related_destination import RelatedDestination
        from .related_device import RelatedDevice
        from .related_malware import RelatedMalware
        from .related_process import RelatedProcess
        from .related_remote_network import RelatedRemoteNetwork
        from .related_tenant import RelatedTenant
        from .related_threat_intelligence import RelatedThreatIntelligence
        from .related_token import RelatedToken
        from .related_user import RelatedUser
        from .related_web_category import RelatedWebCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_additional_data_value(self.additional_data)
    


from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_severity import AlertSeverity
    from .impacted_asset import ImpactedAsset

@dataclass
class AlertTemplate(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The category property
    category: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The impactedAssets property
    impacted_assets: Optional[List[ImpactedAsset]] = None
    # The mitreTechniques property
    mitre_techniques: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recommendedActions property
    recommended_actions: Optional[str] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AlertTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_severity import AlertSeverity
        from .impacted_asset import ImpactedAsset

        from .alert_severity import AlertSeverity
        from .impacted_asset import ImpactedAsset

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "impactedAssets": lambda n : setattr(self, 'impacted_assets', n.get_collection_of_object_values(ImpactedAsset)),
            "mitreTechniques": lambda n : setattr(self, 'mitre_techniques', n.get_collection_of_primitive_values(str)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("impactedAssets", self.impacted_assets)
        writer.write_collection_of_primitive_values("mitreTechniques", self.mitre_techniques)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    


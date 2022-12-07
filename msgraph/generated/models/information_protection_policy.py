from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
information_protection_label = lazy_import('msgraph.generated.models.information_protection_label')

class InformationProtectionPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new informationProtectionPolicy and sets the default values.
        """
        super().__init__()
        # The labels property
        self._labels: Optional[List[information_protection_label.InformationProtectionLabel]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InformationProtectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InformationProtectionPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InformationProtectionPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_object_values(information_protection_label.InformationProtectionLabel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def labels(self,) -> Optional[List[information_protection_label.InformationProtectionLabel]]:
        """
        Gets the labels property value. The labels property
        Returns: Optional[List[information_protection_label.InformationProtectionLabel]]
        """
        return self._labels
    
    @labels.setter
    def labels(self,value: Optional[List[information_protection_label.InformationProtectionLabel]] = None) -> None:
        """
        Sets the labels property value. The labels property
        Args:
            value: Value to set for the labels property.
        """
        self._labels = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("labels", self.labels)
    


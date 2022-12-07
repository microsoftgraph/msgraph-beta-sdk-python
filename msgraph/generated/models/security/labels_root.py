from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
retention_label = lazy_import('msgraph.generated.models.security.retention_label')

class LabelsRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new labelsRoot and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The retentionLabels property
        self._retention_labels: Optional[List[retention_label.RetentionLabel]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LabelsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LabelsRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LabelsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "retention_labels": lambda n : setattr(self, 'retention_labels', n.get_collection_of_object_values(retention_label.RetentionLabel)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def retention_labels(self,) -> Optional[List[retention_label.RetentionLabel]]:
        """
        Gets the retentionLabels property value. The retentionLabels property
        Returns: Optional[List[retention_label.RetentionLabel]]
        """
        return self._retention_labels
    
    @retention_labels.setter
    def retention_labels(self,value: Optional[List[retention_label.RetentionLabel]] = None) -> None:
        """
        Sets the retentionLabels property value. The retentionLabels property
        Args:
            value: Value to set for the retentionLabels property.
        """
        self._retention_labels = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("retentionLabels", self.retention_labels)
    


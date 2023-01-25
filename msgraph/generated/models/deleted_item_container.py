from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
workflow = lazy_import('msgraph.generated.models.identity_governance.workflow')

class DeletedItemContainer(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new deletedItemContainer and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Deleted workflows that end up in the deletedItemsContainer.
        self._workflows: Optional[List[workflow.Workflow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeletedItemContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeletedItemContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeletedItemContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "workflows": lambda n : setattr(self, 'workflows', n.get_collection_of_object_values(workflow.Workflow)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("workflows", self.workflows)
    
    @property
    def workflows(self,) -> Optional[List[workflow.Workflow]]:
        """
        Gets the workflows property value. Deleted workflows that end up in the deletedItemsContainer.
        Returns: Optional[List[workflow.Workflow]]
        """
        return self._workflows
    
    @workflows.setter
    def workflows(self,value: Optional[List[workflow.Workflow]] = None) -> None:
        """
        Sets the workflows property value. Deleted workflows that end up in the deletedItemsContainer.
        Args:
            value: Value to set for the workflows property.
        """
        self._workflows = value
    


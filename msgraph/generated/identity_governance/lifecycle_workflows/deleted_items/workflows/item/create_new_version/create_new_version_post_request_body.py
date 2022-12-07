from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workflow = lazy_import('msgraph.generated.models.identity_governance.workflow')

class CreateNewVersionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the createNewVersion method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new createNewVersionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The workflow property
        self._workflow: Optional[workflow.Workflow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateNewVersionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreateNewVersionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreateNewVersionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "workflow": lambda n : setattr(self, 'workflow', n.get_object_value(workflow.Workflow)),
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
        writer.write_object_value("workflow", self.workflow)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def workflow(self,) -> Optional[workflow.Workflow]:
        """
        Gets the workflow property value. The workflow property
        Returns: Optional[workflow.Workflow]
        """
        return self._workflow
    
    @workflow.setter
    def workflow(self,value: Optional[workflow.Workflow] = None) -> None:
        """
        Sets the workflow property value. The workflow property
        Args:
            value: Value to set for the workflow property.
        """
        self._workflow = value
    


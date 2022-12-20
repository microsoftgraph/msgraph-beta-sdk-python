from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_custom_extension_stage = lazy_import('msgraph.generated.models.access_package_custom_extension_stage')
custom_access_package_workflow_extension = lazy_import('msgraph.generated.models.custom_access_package_workflow_extension')
entity = lazy_import('msgraph.generated.models.entity')

class CustomExtensionHandler(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new customExtensionHandler and sets the default values.
        """
        super().__init__()
        # Indicates which custom workflow extension will be executed at this stage. Nullable. Supports $expand.
        self._custom_extension: Optional[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the stage of the access package assignment request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        self._stage: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionHandler
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionHandler()
    
    @property
    def custom_extension(self,) -> Optional[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]:
        """
        Gets the customExtension property value. Indicates which custom workflow extension will be executed at this stage. Nullable. Supports $expand.
        Returns: Optional[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension]
        """
        return self._custom_extension
    
    @custom_extension.setter
    def custom_extension(self,value: Optional[custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension] = None) -> None:
        """
        Sets the customExtension property value. Indicates which custom workflow extension will be executed at this stage. Nullable. Supports $expand.
        Args:
            value: Value to set for the customExtension property.
        """
        self._custom_extension = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_extension": lambda n : setattr(self, 'custom_extension', n.get_object_value(custom_access_package_workflow_extension.CustomAccessPackageWorkflowExtension)),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(access_package_custom_extension_stage.AccessPackageCustomExtensionStage)),
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
        writer.write_object_value("customExtension", self.custom_extension)
        writer.write_enum_value("stage", self.stage)
    
    @property
    def stage(self,) -> Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]:
        """
        Gets the stage property value. Indicates the stage of the access package assignment request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        Returns: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]
        """
        return self._stage
    
    @stage.setter
    def stage(self,value: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None) -> None:
        """
        Sets the stage property value. Indicates the stage of the access package assignment request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        Args:
            value: Value to set for the stage property.
        """
        self._stage = value
    


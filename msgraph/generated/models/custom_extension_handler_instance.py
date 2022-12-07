from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_custom_extension_handler_status = lazy_import('msgraph.generated.models.access_package_custom_extension_handler_status')
access_package_custom_extension_stage = lazy_import('msgraph.generated.models.access_package_custom_extension_stage')

class CustomExtensionHandlerInstance(AdditionalDataHolder, Parsable):
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
        Instantiates a new customExtensionHandlerInstance and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifier of the customAccessPackageWorkflowExtension triggered at this instance.
        self._custom_extension_id: Optional[str] = None
        # The unique run ID for the logic app.
        self._external_correlation_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the stage of the request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        self._stage: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None
        # Status of the request to run the access package custom extension workflow that is associated with the logic app. The possible values are: requestSent, requestReceived, unknownFutureValue.
        self._status: Optional[access_package_custom_extension_handler_status.AccessPackageCustomExtensionHandlerStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionHandlerInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionHandlerInstance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomExtensionHandlerInstance()
    
    @property
    def custom_extension_id(self,) -> Optional[str]:
        """
        Gets the customExtensionId property value. Identifier of the customAccessPackageWorkflowExtension triggered at this instance.
        Returns: Optional[str]
        """
        return self._custom_extension_id
    
    @custom_extension_id.setter
    def custom_extension_id(self,value: Optional[str] = None) -> None:
        """
        Sets the customExtensionId property value. Identifier of the customAccessPackageWorkflowExtension triggered at this instance.
        Args:
            value: Value to set for the customExtensionId property.
        """
        self._custom_extension_id = value
    
    @property
    def external_correlation_id(self,) -> Optional[str]:
        """
        Gets the externalCorrelationId property value. The unique run ID for the logic app.
        Returns: Optional[str]
        """
        return self._external_correlation_id
    
    @external_correlation_id.setter
    def external_correlation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalCorrelationId property value. The unique run ID for the logic app.
        Args:
            value: Value to set for the externalCorrelationId property.
        """
        self._external_correlation_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_extension_id": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "external_correlation_id": lambda n : setattr(self, 'external_correlation_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(access_package_custom_extension_stage.AccessPackageCustomExtensionStage)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(access_package_custom_extension_handler_status.AccessPackageCustomExtensionHandlerStatus)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_str_value("externalCorrelationId", self.external_correlation_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("stage", self.stage)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def stage(self,) -> Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]:
        """
        Gets the stage property value. Indicates the stage of the request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        Returns: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage]
        """
        return self._stage
    
    @stage.setter
    def stage(self,value: Optional[access_package_custom_extension_stage.AccessPackageCustomExtensionStage] = None) -> None:
        """
        Sets the stage property value. Indicates the stage of the request workflow when the access package custom extension runs. The possible values are: assignmentRequestCreated, assignmentRequestApproved, assignmentRequestGranted, assignmentRequestRemoved, assignmentFourteenDaysBeforeExpiration, assignmentOneDayBeforeExpiration, unknownFutureValue.
        Args:
            value: Value to set for the stage property.
        """
        self._stage = value
    
    @property
    def status(self,) -> Optional[access_package_custom_extension_handler_status.AccessPackageCustomExtensionHandlerStatus]:
        """
        Gets the status property value. Status of the request to run the access package custom extension workflow that is associated with the logic app. The possible values are: requestSent, requestReceived, unknownFutureValue.
        Returns: Optional[access_package_custom_extension_handler_status.AccessPackageCustomExtensionHandlerStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[access_package_custom_extension_handler_status.AccessPackageCustomExtensionHandlerStatus] = None) -> None:
        """
        Sets the status property value. Status of the request to run the access package custom extension workflow that is associated with the logic app. The possible values are: requestSent, requestReceived, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    


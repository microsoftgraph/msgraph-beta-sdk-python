from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import on_premises_accidental_deletion_prevention, on_premises_current_export_data, on_premises_writeback_configuration

class OnPremisesDirectorySynchronizationConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesDirectorySynchronizationConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Contains the accidental deletion prevention configuration for a tenant.
        self._accidental_deletion_prevention: Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention] = None
        # The anchor attribute allows customers to customize the property used to create source anchors for synchronization enabled objects.
        self._anchor_attribute: Optional[str] = None
        # The identifier of the on-premises directory synchronization client application that is configured for the tenant.
        self._application_id: Optional[str] = None
        # Data for the current export run.
        self._current_export_data: Optional[on_premises_current_export_data.OnPremisesCurrentExportData] = None
        # Interval of time that the customer requested the sync client waits between sync cycles.
        self._customer_requested_synchronization_interval: Optional[timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the version of the on-premises directory synchronization application.
        self._synchronization_client_version: Optional[str] = None
        # Interval of time the sync client should honor between sync cycles
        self._synchronization_interval: Optional[timedelta] = None
        # Configuration to control how cloud created or owned objects are synchronized back to the on-premises directory.
        self._writeback_configuration: Optional[on_premises_writeback_configuration.OnPremisesWritebackConfiguration] = None
    
    @property
    def accidental_deletion_prevention(self,) -> Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention]:
        """
        Gets the accidentalDeletionPrevention property value. Contains the accidental deletion prevention configuration for a tenant.
        Returns: Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention]
        """
        return self._accidental_deletion_prevention
    
    @accidental_deletion_prevention.setter
    def accidental_deletion_prevention(self,value: Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention] = None) -> None:
        """
        Sets the accidentalDeletionPrevention property value. Contains the accidental deletion prevention configuration for a tenant.
        Args:
            value: Value to set for the accidental_deletion_prevention property.
        """
        self._accidental_deletion_prevention = value
    
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
    
    @property
    def anchor_attribute(self,) -> Optional[str]:
        """
        Gets the anchorAttribute property value. The anchor attribute allows customers to customize the property used to create source anchors for synchronization enabled objects.
        Returns: Optional[str]
        """
        return self._anchor_attribute
    
    @anchor_attribute.setter
    def anchor_attribute(self,value: Optional[str] = None) -> None:
        """
        Sets the anchorAttribute property value. The anchor attribute allows customers to customize the property used to create source anchors for synchronization enabled objects.
        Args:
            value: Value to set for the anchor_attribute property.
        """
        self._anchor_attribute = value
    
    @property
    def application_id(self,) -> Optional[str]:
        """
        Gets the applicationId property value. The identifier of the on-premises directory synchronization client application that is configured for the tenant.
        Returns: Optional[str]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationId property value. The identifier of the on-premises directory synchronization client application that is configured for the tenant.
        Args:
            value: Value to set for the application_id property.
        """
        self._application_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesDirectorySynchronizationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronizationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesDirectorySynchronizationConfiguration()
    
    @property
    def current_export_data(self,) -> Optional[on_premises_current_export_data.OnPremisesCurrentExportData]:
        """
        Gets the currentExportData property value. Data for the current export run.
        Returns: Optional[on_premises_current_export_data.OnPremisesCurrentExportData]
        """
        return self._current_export_data
    
    @current_export_data.setter
    def current_export_data(self,value: Optional[on_premises_current_export_data.OnPremisesCurrentExportData] = None) -> None:
        """
        Sets the currentExportData property value. Data for the current export run.
        Args:
            value: Value to set for the current_export_data property.
        """
        self._current_export_data = value
    
    @property
    def customer_requested_synchronization_interval(self,) -> Optional[timedelta]:
        """
        Gets the customerRequestedSynchronizationInterval property value. Interval of time that the customer requested the sync client waits between sync cycles.
        Returns: Optional[timedelta]
        """
        return self._customer_requested_synchronization_interval
    
    @customer_requested_synchronization_interval.setter
    def customer_requested_synchronization_interval(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the customerRequestedSynchronizationInterval property value. Interval of time that the customer requested the sync client waits between sync cycles.
        Args:
            value: Value to set for the customer_requested_synchronization_interval property.
        """
        self._customer_requested_synchronization_interval = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import on_premises_accidental_deletion_prevention, on_premises_current_export_data, on_premises_writeback_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "accidentalDeletionPrevention": lambda n : setattr(self, 'accidental_deletion_prevention', n.get_object_value(on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention)),
            "anchorAttribute": lambda n : setattr(self, 'anchor_attribute', n.get_str_value()),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "currentExportData": lambda n : setattr(self, 'current_export_data', n.get_object_value(on_premises_current_export_data.OnPremisesCurrentExportData)),
            "customerRequestedSynchronizationInterval": lambda n : setattr(self, 'customer_requested_synchronization_interval', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "synchronizationClientVersion": lambda n : setattr(self, 'synchronization_client_version', n.get_str_value()),
            "synchronizationInterval": lambda n : setattr(self, 'synchronization_interval', n.get_timedelta_value()),
            "writebackConfiguration": lambda n : setattr(self, 'writeback_configuration', n.get_object_value(on_premises_writeback_configuration.OnPremisesWritebackConfiguration)),
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
            value: Value to set for the odata_type property.
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
        writer.write_object_value("accidentalDeletionPrevention", self.accidental_deletion_prevention)
        writer.write_str_value("anchorAttribute", self.anchor_attribute)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_object_value("currentExportData", self.current_export_data)
        writer.write_timedelta_value("customerRequestedSynchronizationInterval", self.customer_requested_synchronization_interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("synchronizationClientVersion", self.synchronization_client_version)
        writer.write_timedelta_value("synchronizationInterval", self.synchronization_interval)
        writer.write_object_value("writebackConfiguration", self.writeback_configuration)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def synchronization_client_version(self,) -> Optional[str]:
        """
        Gets the synchronizationClientVersion property value. Indicates the version of the on-premises directory synchronization application.
        Returns: Optional[str]
        """
        return self._synchronization_client_version
    
    @synchronization_client_version.setter
    def synchronization_client_version(self,value: Optional[str] = None) -> None:
        """
        Sets the synchronizationClientVersion property value. Indicates the version of the on-premises directory synchronization application.
        Args:
            value: Value to set for the synchronization_client_version property.
        """
        self._synchronization_client_version = value
    
    @property
    def synchronization_interval(self,) -> Optional[timedelta]:
        """
        Gets the synchronizationInterval property value. Interval of time the sync client should honor between sync cycles
        Returns: Optional[timedelta]
        """
        return self._synchronization_interval
    
    @synchronization_interval.setter
    def synchronization_interval(self,value: Optional[timedelta] = None) -> None:
        """
        Sets the synchronizationInterval property value. Interval of time the sync client should honor between sync cycles
        Args:
            value: Value to set for the synchronization_interval property.
        """
        self._synchronization_interval = value
    
    @property
    def writeback_configuration(self,) -> Optional[on_premises_writeback_configuration.OnPremisesWritebackConfiguration]:
        """
        Gets the writebackConfiguration property value. Configuration to control how cloud created or owned objects are synchronized back to the on-premises directory.
        Returns: Optional[on_premises_writeback_configuration.OnPremisesWritebackConfiguration]
        """
        return self._writeback_configuration
    
    @writeback_configuration.setter
    def writeback_configuration(self,value: Optional[on_premises_writeback_configuration.OnPremisesWritebackConfiguration] = None) -> None:
        """
        Sets the writebackConfiguration property value. Configuration to control how cloud created or owned objects are synchronized back to the on-premises directory.
        Args:
            value: Value to set for the writeback_configuration property.
        """
        self._writeback_configuration = value
    


from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')
win32_lob_app_detection = lazy_import('msgraph.generated.models.win32_lob_app_detection')
win32_lob_app_install_experience = lazy_import('msgraph.generated.models.win32_lob_app_install_experience')
win32_lob_app_msi_information = lazy_import('msgraph.generated.models.win32_lob_app_msi_information')
win32_lob_app_requirement = lazy_import('msgraph.generated.models.win32_lob_app_requirement')
win32_lob_app_return_code = lazy_import('msgraph.generated.models.win32_lob_app_return_code')
win32_lob_app_rule = lazy_import('msgraph.generated.models.win32_lob_app_rule')
windows_architecture = lazy_import('msgraph.generated.models.windows_architecture')
windows_minimum_operating_system = lazy_import('msgraph.generated.models.windows_minimum_operating_system')

class Win32LobApp(mobile_lob_app.MobileLobApp):
    @property
    def allow_available_uninstall(self,) -> Optional[bool]:
        """
        Gets the allowAvailableUninstall property value. When TRUE, indicates that uninstall is supported from the company portal for the Windows app (Win32) with an Available assignment. When FALSE, indicates that uninstall is not supported for the Windows app (Win32) with an Available assignment. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._allow_available_uninstall
    
    @allow_available_uninstall.setter
    def allow_available_uninstall(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAvailableUninstall property value. When TRUE, indicates that uninstall is supported from the company portal for the Windows app (Win32) with an Available assignment. When FALSE, indicates that uninstall is not supported for the Windows app (Win32) with an Available assignment. Default value is FALSE.
        Args:
            value: Value to set for the allowAvailableUninstall property.
        """
        self._allow_available_uninstall = value
    
    @property
    def applicable_architectures(self,) -> Optional[windows_architecture.WindowsArchitecture]:
        """
        Gets the applicableArchitectures property value. Contains properties for Windows architecture.
        Returns: Optional[windows_architecture.WindowsArchitecture]
        """
        return self._applicable_architectures
    
    @applicable_architectures.setter
    def applicable_architectures(self,value: Optional[windows_architecture.WindowsArchitecture] = None) -> None:
        """
        Sets the applicableArchitectures property value. Contains properties for Windows architecture.
        Args:
            value: Value to set for the applicableArchitectures property.
        """
        self._applicable_architectures = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Win32LobApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.win32LobApp"
        # When TRUE, indicates that uninstall is supported from the company portal for the Windows app (Win32) with an Available assignment. When FALSE, indicates that uninstall is not supported for the Windows app (Win32) with an Available assignment. Default value is FALSE.
        self._allow_available_uninstall: Optional[bool] = None
        # Contains properties for Windows architecture.
        self._applicable_architectures: Optional[windows_architecture.WindowsArchitecture] = None
        # The detection rules to detect Win32 Line of Business (LoB) app.
        self._detection_rules: Optional[List[win32_lob_app_detection.Win32LobAppDetection]] = None
        # The version displayed in the UX for this app.
        self._display_version: Optional[str] = None
        # The command line to install this app
        self._install_command_line: Optional[str] = None
        # The install experience for this app.
        self._install_experience: Optional[win32_lob_app_install_experience.Win32LobAppInstallExperience] = None
        # The value for the minimum CPU speed which is required to install this app.
        self._minimum_cpu_speed_in_m_hz: Optional[int] = None
        # The value for the minimum free disk space which is required to install this app.
        self._minimum_free_disk_space_in_m_b: Optional[int] = None
        # The value for the minimum physical memory which is required to install this app.
        self._minimum_memory_in_m_b: Optional[int] = None
        # The value for the minimum number of processors which is required to install this app.
        self._minimum_number_of_processors: Optional[int] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None
        # The value for the minimum supported windows release.
        self._minimum_supported_windows_release: Optional[str] = None
        # The MSI details if this Win32 app is an MSI app.
        self._msi_information: Optional[win32_lob_app_msi_information.Win32LobAppMsiInformation] = None
        # The requirement rules to detect Win32 Line of Business (LoB) app.
        self._requirement_rules: Optional[List[win32_lob_app_requirement.Win32LobAppRequirement]] = None
        # The return codes for post installation behavior.
        self._return_codes: Optional[List[win32_lob_app_return_code.Win32LobAppReturnCode]] = None
        # The detection and requirement rules for this app.
        self._rules: Optional[List[win32_lob_app_rule.Win32LobAppRule]] = None
        # The relative path of the setup file in the encrypted Win32LobApp package.
        self._setup_file_path: Optional[str] = None
        # The command line to uninstall this app
        self._uninstall_command_line: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Win32LobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Win32LobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Win32LobApp()
    
    @property
    def detection_rules(self,) -> Optional[List[win32_lob_app_detection.Win32LobAppDetection]]:
        """
        Gets the detectionRules property value. The detection rules to detect Win32 Line of Business (LoB) app.
        Returns: Optional[List[win32_lob_app_detection.Win32LobAppDetection]]
        """
        return self._detection_rules
    
    @detection_rules.setter
    def detection_rules(self,value: Optional[List[win32_lob_app_detection.Win32LobAppDetection]] = None) -> None:
        """
        Sets the detectionRules property value. The detection rules to detect Win32 Line of Business (LoB) app.
        Args:
            value: Value to set for the detectionRules property.
        """
        self._detection_rules = value
    
    @property
    def display_version(self,) -> Optional[str]:
        """
        Gets the displayVersion property value. The version displayed in the UX for this app.
        Returns: Optional[str]
        """
        return self._display_version
    
    @display_version.setter
    def display_version(self,value: Optional[str] = None) -> None:
        """
        Sets the displayVersion property value. The version displayed in the UX for this app.
        Args:
            value: Value to set for the displayVersion property.
        """
        self._display_version = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_available_uninstall": lambda n : setattr(self, 'allow_available_uninstall', n.get_bool_value()),
            "applicable_architectures": lambda n : setattr(self, 'applicable_architectures', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "detection_rules": lambda n : setattr(self, 'detection_rules', n.get_collection_of_object_values(win32_lob_app_detection.Win32LobAppDetection)),
            "display_version": lambda n : setattr(self, 'display_version', n.get_str_value()),
            "install_command_line": lambda n : setattr(self, 'install_command_line', n.get_str_value()),
            "install_experience": lambda n : setattr(self, 'install_experience', n.get_object_value(win32_lob_app_install_experience.Win32LobAppInstallExperience)),
            "minimum_cpu_speed_in_m_hz": lambda n : setattr(self, 'minimum_cpu_speed_in_m_hz', n.get_int_value()),
            "minimum_free_disk_space_in_m_b": lambda n : setattr(self, 'minimum_free_disk_space_in_m_b', n.get_int_value()),
            "minimum_memory_in_m_b": lambda n : setattr(self, 'minimum_memory_in_m_b', n.get_int_value()),
            "minimum_number_of_processors": lambda n : setattr(self, 'minimum_number_of_processors', n.get_int_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(windows_minimum_operating_system.WindowsMinimumOperatingSystem)),
            "minimum_supported_windows_release": lambda n : setattr(self, 'minimum_supported_windows_release', n.get_str_value()),
            "msi_information": lambda n : setattr(self, 'msi_information', n.get_object_value(win32_lob_app_msi_information.Win32LobAppMsiInformation)),
            "requirement_rules": lambda n : setattr(self, 'requirement_rules', n.get_collection_of_object_values(win32_lob_app_requirement.Win32LobAppRequirement)),
            "return_codes": lambda n : setattr(self, 'return_codes', n.get_collection_of_object_values(win32_lob_app_return_code.Win32LobAppReturnCode)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(win32_lob_app_rule.Win32LobAppRule)),
            "setup_file_path": lambda n : setattr(self, 'setup_file_path', n.get_str_value()),
            "uninstall_command_line": lambda n : setattr(self, 'uninstall_command_line', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def install_command_line(self,) -> Optional[str]:
        """
        Gets the installCommandLine property value. The command line to install this app
        Returns: Optional[str]
        """
        return self._install_command_line
    
    @install_command_line.setter
    def install_command_line(self,value: Optional[str] = None) -> None:
        """
        Sets the installCommandLine property value. The command line to install this app
        Args:
            value: Value to set for the installCommandLine property.
        """
        self._install_command_line = value
    
    @property
    def install_experience(self,) -> Optional[win32_lob_app_install_experience.Win32LobAppInstallExperience]:
        """
        Gets the installExperience property value. The install experience for this app.
        Returns: Optional[win32_lob_app_install_experience.Win32LobAppInstallExperience]
        """
        return self._install_experience
    
    @install_experience.setter
    def install_experience(self,value: Optional[win32_lob_app_install_experience.Win32LobAppInstallExperience] = None) -> None:
        """
        Sets the installExperience property value. The install experience for this app.
        Args:
            value: Value to set for the installExperience property.
        """
        self._install_experience = value
    
    @property
    def minimum_cpu_speed_in_m_hz(self,) -> Optional[int]:
        """
        Gets the minimumCpuSpeedInMHz property value. The value for the minimum CPU speed which is required to install this app.
        Returns: Optional[int]
        """
        return self._minimum_cpu_speed_in_m_hz
    
    @minimum_cpu_speed_in_m_hz.setter
    def minimum_cpu_speed_in_m_hz(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumCpuSpeedInMHz property value. The value for the minimum CPU speed which is required to install this app.
        Args:
            value: Value to set for the minimumCpuSpeedInMHz property.
        """
        self._minimum_cpu_speed_in_m_hz = value
    
    @property
    def minimum_free_disk_space_in_m_b(self,) -> Optional[int]:
        """
        Gets the minimumFreeDiskSpaceInMB property value. The value for the minimum free disk space which is required to install this app.
        Returns: Optional[int]
        """
        return self._minimum_free_disk_space_in_m_b
    
    @minimum_free_disk_space_in_m_b.setter
    def minimum_free_disk_space_in_m_b(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumFreeDiskSpaceInMB property value. The value for the minimum free disk space which is required to install this app.
        Args:
            value: Value to set for the minimumFreeDiskSpaceInMB property.
        """
        self._minimum_free_disk_space_in_m_b = value
    
    @property
    def minimum_memory_in_m_b(self,) -> Optional[int]:
        """
        Gets the minimumMemoryInMB property value. The value for the minimum physical memory which is required to install this app.
        Returns: Optional[int]
        """
        return self._minimum_memory_in_m_b
    
    @minimum_memory_in_m_b.setter
    def minimum_memory_in_m_b(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumMemoryInMB property value. The value for the minimum physical memory which is required to install this app.
        Args:
            value: Value to set for the minimumMemoryInMB property.
        """
        self._minimum_memory_in_m_b = value
    
    @property
    def minimum_number_of_processors(self,) -> Optional[int]:
        """
        Gets the minimumNumberOfProcessors property value. The value for the minimum number of processors which is required to install this app.
        Returns: Optional[int]
        """
        return self._minimum_number_of_processors
    
    @minimum_number_of_processors.setter
    def minimum_number_of_processors(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumNumberOfProcessors property value. The value for the minimum number of processors which is required to install this app.
        Args:
            value: Value to set for the minimumNumberOfProcessors property.
        """
        self._minimum_number_of_processors = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def minimum_supported_windows_release(self,) -> Optional[str]:
        """
        Gets the minimumSupportedWindowsRelease property value. The value for the minimum supported windows release.
        Returns: Optional[str]
        """
        return self._minimum_supported_windows_release
    
    @minimum_supported_windows_release.setter
    def minimum_supported_windows_release(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumSupportedWindowsRelease property value. The value for the minimum supported windows release.
        Args:
            value: Value to set for the minimumSupportedWindowsRelease property.
        """
        self._minimum_supported_windows_release = value
    
    @property
    def msi_information(self,) -> Optional[win32_lob_app_msi_information.Win32LobAppMsiInformation]:
        """
        Gets the msiInformation property value. The MSI details if this Win32 app is an MSI app.
        Returns: Optional[win32_lob_app_msi_information.Win32LobAppMsiInformation]
        """
        return self._msi_information
    
    @msi_information.setter
    def msi_information(self,value: Optional[win32_lob_app_msi_information.Win32LobAppMsiInformation] = None) -> None:
        """
        Sets the msiInformation property value. The MSI details if this Win32 app is an MSI app.
        Args:
            value: Value to set for the msiInformation property.
        """
        self._msi_information = value
    
    @property
    def requirement_rules(self,) -> Optional[List[win32_lob_app_requirement.Win32LobAppRequirement]]:
        """
        Gets the requirementRules property value. The requirement rules to detect Win32 Line of Business (LoB) app.
        Returns: Optional[List[win32_lob_app_requirement.Win32LobAppRequirement]]
        """
        return self._requirement_rules
    
    @requirement_rules.setter
    def requirement_rules(self,value: Optional[List[win32_lob_app_requirement.Win32LobAppRequirement]] = None) -> None:
        """
        Sets the requirementRules property value. The requirement rules to detect Win32 Line of Business (LoB) app.
        Args:
            value: Value to set for the requirementRules property.
        """
        self._requirement_rules = value
    
    @property
    def return_codes(self,) -> Optional[List[win32_lob_app_return_code.Win32LobAppReturnCode]]:
        """
        Gets the returnCodes property value. The return codes for post installation behavior.
        Returns: Optional[List[win32_lob_app_return_code.Win32LobAppReturnCode]]
        """
        return self._return_codes
    
    @return_codes.setter
    def return_codes(self,value: Optional[List[win32_lob_app_return_code.Win32LobAppReturnCode]] = None) -> None:
        """
        Sets the returnCodes property value. The return codes for post installation behavior.
        Args:
            value: Value to set for the returnCodes property.
        """
        self._return_codes = value
    
    @property
    def rules(self,) -> Optional[List[win32_lob_app_rule.Win32LobAppRule]]:
        """
        Gets the rules property value. The detection and requirement rules for this app.
        Returns: Optional[List[win32_lob_app_rule.Win32LobAppRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[win32_lob_app_rule.Win32LobAppRule]] = None) -> None:
        """
        Sets the rules property value. The detection and requirement rules for this app.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowAvailableUninstall", self.allow_available_uninstall)
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_collection_of_object_values("detectionRules", self.detection_rules)
        writer.write_str_value("displayVersion", self.display_version)
        writer.write_str_value("installCommandLine", self.install_command_line)
        writer.write_object_value("installExperience", self.install_experience)
        writer.write_int_value("minimumCpuSpeedInMHz", self.minimum_cpu_speed_in_m_hz)
        writer.write_int_value("minimumFreeDiskSpaceInMB", self.minimum_free_disk_space_in_m_b)
        writer.write_int_value("minimumMemoryInMB", self.minimum_memory_in_m_b)
        writer.write_int_value("minimumNumberOfProcessors", self.minimum_number_of_processors)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("minimumSupportedWindowsRelease", self.minimum_supported_windows_release)
        writer.write_object_value("msiInformation", self.msi_information)
        writer.write_collection_of_object_values("requirementRules", self.requirement_rules)
        writer.write_collection_of_object_values("returnCodes", self.return_codes)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_str_value("setupFilePath", self.setup_file_path)
        writer.write_str_value("uninstallCommandLine", self.uninstall_command_line)
    
    @property
    def setup_file_path(self,) -> Optional[str]:
        """
        Gets the setupFilePath property value. The relative path of the setup file in the encrypted Win32LobApp package.
        Returns: Optional[str]
        """
        return self._setup_file_path
    
    @setup_file_path.setter
    def setup_file_path(self,value: Optional[str] = None) -> None:
        """
        Sets the setupFilePath property value. The relative path of the setup file in the encrypted Win32LobApp package.
        Args:
            value: Value to set for the setupFilePath property.
        """
        self._setup_file_path = value
    
    @property
    def uninstall_command_line(self,) -> Optional[str]:
        """
        Gets the uninstallCommandLine property value. The command line to uninstall this app
        Returns: Optional[str]
        """
        return self._uninstall_command_line
    
    @uninstall_command_line.setter
    def uninstall_command_line(self,value: Optional[str] = None) -> None:
        """
        Sets the uninstallCommandLine property value. The command line to uninstall this app
        Args:
            value: Value to set for the uninstallCommandLine property.
        """
        self._uninstall_command_line = value
    


from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

enablement = lazy_import('msgraph.generated.models.enablement')
mac_o_s_apple_event_receiver = lazy_import('msgraph.generated.models.mac_o_s_apple_event_receiver')
mac_o_s_process_identifier_type = lazy_import('msgraph.generated.models.mac_o_s_process_identifier_type')

class MacOSPrivacyAccessControlItem(AdditionalDataHolder, Parsable):
    """
    Represents per-process privacy preferences.
    """
    @property
    def accessibility(self,) -> Optional[enablement.Enablement]:
        """
        Gets the accessibility property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._accessibility
    
    @accessibility.setter
    def accessibility(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the accessibility property value. Possible values of a property
        Args:
            value: Value to set for the accessibility property.
        """
        self._accessibility = value
    
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
    def address_book(self,) -> Optional[enablement.Enablement]:
        """
        Gets the addressBook property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._address_book
    
    @address_book.setter
    def address_book(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the addressBook property value. Possible values of a property
        Args:
            value: Value to set for the addressBook property.
        """
        self._address_book = value
    
    @property
    def apple_events_allowed_receivers(self,) -> Optional[List[mac_o_s_apple_event_receiver.MacOSAppleEventReceiver]]:
        """
        Gets the appleEventsAllowedReceivers property value. Allow or deny the app or process to send a restricted Apple event to another app or process. You will need to know the identifier, identifier type, and code requirement of the receiving app or process. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[mac_o_s_apple_event_receiver.MacOSAppleEventReceiver]]
        """
        return self._apple_events_allowed_receivers
    
    @apple_events_allowed_receivers.setter
    def apple_events_allowed_receivers(self,value: Optional[List[mac_o_s_apple_event_receiver.MacOSAppleEventReceiver]] = None) -> None:
        """
        Sets the appleEventsAllowedReceivers property value. Allow or deny the app or process to send a restricted Apple event to another app or process. You will need to know the identifier, identifier type, and code requirement of the receiving app or process. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the appleEventsAllowedReceivers property.
        """
        self._apple_events_allowed_receivers = value
    
    @property
    def block_camera(self,) -> Optional[bool]:
        """
        Gets the blockCamera property value. Block access to camera app.
        Returns: Optional[bool]
        """
        return self._block_camera
    
    @block_camera.setter
    def block_camera(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockCamera property value. Block access to camera app.
        Args:
            value: Value to set for the blockCamera property.
        """
        self._block_camera = value
    
    @property
    def block_listen_event(self,) -> Optional[bool]:
        """
        Gets the blockListenEvent property value. Block the app or process from listening to events from input devices such as mouse, keyboard, and trackpad.Requires macOS 10.15 or later.
        Returns: Optional[bool]
        """
        return self._block_listen_event
    
    @block_listen_event.setter
    def block_listen_event(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockListenEvent property value. Block the app or process from listening to events from input devices such as mouse, keyboard, and trackpad.Requires macOS 10.15 or later.
        Args:
            value: Value to set for the blockListenEvent property.
        """
        self._block_listen_event = value
    
    @property
    def block_microphone(self,) -> Optional[bool]:
        """
        Gets the blockMicrophone property value. Block access to microphone.
        Returns: Optional[bool]
        """
        return self._block_microphone
    
    @block_microphone.setter
    def block_microphone(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockMicrophone property value. Block access to microphone.
        Args:
            value: Value to set for the blockMicrophone property.
        """
        self._block_microphone = value
    
    @property
    def block_screen_capture(self,) -> Optional[bool]:
        """
        Gets the blockScreenCapture property value. Block app from capturing contents of system display. Requires macOS 10.15 or later.
        Returns: Optional[bool]
        """
        return self._block_screen_capture
    
    @block_screen_capture.setter
    def block_screen_capture(self,value: Optional[bool] = None) -> None:
        """
        Sets the blockScreenCapture property value. Block app from capturing contents of system display. Requires macOS 10.15 or later.
        Args:
            value: Value to set for the blockScreenCapture property.
        """
        self._block_screen_capture = value
    
    @property
    def calendar(self,) -> Optional[enablement.Enablement]:
        """
        Gets the calendar property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._calendar
    
    @calendar.setter
    def calendar(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the calendar property value. Possible values of a property
        Args:
            value: Value to set for the calendar property.
        """
        self._calendar = value
    
    @property
    def code_requirement(self,) -> Optional[str]:
        """
        Gets the codeRequirement property value. Enter the code requirement, which can be obtained with the command 'codesign –display -r –' in the Terminal app. Include everything after '=>'.
        Returns: Optional[str]
        """
        return self._code_requirement
    
    @code_requirement.setter
    def code_requirement(self,value: Optional[str] = None) -> None:
        """
        Sets the codeRequirement property value. Enter the code requirement, which can be obtained with the command 'codesign –display -r –' in the Terminal app. Include everything after '=>'.
        Args:
            value: Value to set for the codeRequirement property.
        """
        self._code_requirement = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new macOSPrivacyAccessControlItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Possible values of a property
        self._accessibility: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._address_book: Optional[enablement.Enablement] = None
        # Allow or deny the app or process to send a restricted Apple event to another app or process. You will need to know the identifier, identifier type, and code requirement of the receiving app or process. This collection can contain a maximum of 500 elements.
        self._apple_events_allowed_receivers: Optional[List[mac_o_s_apple_event_receiver.MacOSAppleEventReceiver]] = None
        # Block access to camera app.
        self._block_camera: Optional[bool] = None
        # Block the app or process from listening to events from input devices such as mouse, keyboard, and trackpad.Requires macOS 10.15 or later.
        self._block_listen_event: Optional[bool] = None
        # Block access to microphone.
        self._block_microphone: Optional[bool] = None
        # Block app from capturing contents of system display. Requires macOS 10.15 or later.
        self._block_screen_capture: Optional[bool] = None
        # Possible values of a property
        self._calendar: Optional[enablement.Enablement] = None
        # Enter the code requirement, which can be obtained with the command 'codesign –display -r –' in the Terminal app. Include everything after '=>'.
        self._code_requirement: Optional[str] = None
        # The display name of the app, process, or executable.
        self._display_name: Optional[str] = None
        # Possible values of a property
        self._file_provider_presence: Optional[enablement.Enablement] = None
        # The bundle ID or path of the app, process, or executable.
        self._identifier: Optional[str] = None
        # Process identifier types for MacOS Privacy Preferences
        self._identifier_type: Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType] = None
        # Possible values of a property
        self._media_library: Optional[enablement.Enablement] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Possible values of a property
        self._photos: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._post_event: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._reminders: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._speech_recognition: Optional[enablement.Enablement] = None
        # Statically validates the code requirement. Use this setting if the process invalidates its dynamic code signature.
        self._static_code_validation: Optional[bool] = None
        # Possible values of a property
        self._system_policy_all_files: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._system_policy_desktop_folder: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._system_policy_documents_folder: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._system_policy_downloads_folder: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._system_policy_network_volumes: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._system_policy_removable_volumes: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._system_policy_system_admin_files: Optional[enablement.Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSPrivacyAccessControlItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSPrivacyAccessControlItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSPrivacyAccessControlItem()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the app, process, or executable.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the app, process, or executable.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def file_provider_presence(self,) -> Optional[enablement.Enablement]:
        """
        Gets the fileProviderPresence property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._file_provider_presence
    
    @file_provider_presence.setter
    def file_provider_presence(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the fileProviderPresence property value. Possible values of a property
        Args:
            value: Value to set for the fileProviderPresence property.
        """
        self._file_provider_presence = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accessibility": lambda n : setattr(self, 'accessibility', n.get_enum_value(enablement.Enablement)),
            "address_book": lambda n : setattr(self, 'address_book', n.get_enum_value(enablement.Enablement)),
            "apple_events_allowed_receivers": lambda n : setattr(self, 'apple_events_allowed_receivers', n.get_collection_of_object_values(mac_o_s_apple_event_receiver.MacOSAppleEventReceiver)),
            "block_camera": lambda n : setattr(self, 'block_camera', n.get_bool_value()),
            "block_listen_event": lambda n : setattr(self, 'block_listen_event', n.get_bool_value()),
            "block_microphone": lambda n : setattr(self, 'block_microphone', n.get_bool_value()),
            "block_screen_capture": lambda n : setattr(self, 'block_screen_capture', n.get_bool_value()),
            "calendar": lambda n : setattr(self, 'calendar', n.get_enum_value(enablement.Enablement)),
            "code_requirement": lambda n : setattr(self, 'code_requirement', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "file_provider_presence": lambda n : setattr(self, 'file_provider_presence', n.get_enum_value(enablement.Enablement)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "identifier_type": lambda n : setattr(self, 'identifier_type', n.get_enum_value(mac_o_s_process_identifier_type.MacOSProcessIdentifierType)),
            "media_library": lambda n : setattr(self, 'media_library', n.get_enum_value(enablement.Enablement)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "photos": lambda n : setattr(self, 'photos', n.get_enum_value(enablement.Enablement)),
            "post_event": lambda n : setattr(self, 'post_event', n.get_enum_value(enablement.Enablement)),
            "reminders": lambda n : setattr(self, 'reminders', n.get_enum_value(enablement.Enablement)),
            "speech_recognition": lambda n : setattr(self, 'speech_recognition', n.get_enum_value(enablement.Enablement)),
            "static_code_validation": lambda n : setattr(self, 'static_code_validation', n.get_bool_value()),
            "system_policy_all_files": lambda n : setattr(self, 'system_policy_all_files', n.get_enum_value(enablement.Enablement)),
            "system_policy_desktop_folder": lambda n : setattr(self, 'system_policy_desktop_folder', n.get_enum_value(enablement.Enablement)),
            "system_policy_documents_folder": lambda n : setattr(self, 'system_policy_documents_folder', n.get_enum_value(enablement.Enablement)),
            "system_policy_downloads_folder": lambda n : setattr(self, 'system_policy_downloads_folder', n.get_enum_value(enablement.Enablement)),
            "system_policy_network_volumes": lambda n : setattr(self, 'system_policy_network_volumes', n.get_enum_value(enablement.Enablement)),
            "system_policy_removable_volumes": lambda n : setattr(self, 'system_policy_removable_volumes', n.get_enum_value(enablement.Enablement)),
            "system_policy_system_admin_files": lambda n : setattr(self, 'system_policy_system_admin_files', n.get_enum_value(enablement.Enablement)),
        }
        return fields
    
    @property
    def identifier(self,) -> Optional[str]:
        """
        Gets the identifier property value. The bundle ID or path of the app, process, or executable.
        Returns: Optional[str]
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identifier property value. The bundle ID or path of the app, process, or executable.
        Args:
            value: Value to set for the identifier property.
        """
        self._identifier = value
    
    @property
    def identifier_type(self,) -> Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType]:
        """
        Gets the identifierType property value. Process identifier types for MacOS Privacy Preferences
        Returns: Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType]
        """
        return self._identifier_type
    
    @identifier_type.setter
    def identifier_type(self,value: Optional[mac_o_s_process_identifier_type.MacOSProcessIdentifierType] = None) -> None:
        """
        Sets the identifierType property value. Process identifier types for MacOS Privacy Preferences
        Args:
            value: Value to set for the identifierType property.
        """
        self._identifier_type = value
    
    @property
    def media_library(self,) -> Optional[enablement.Enablement]:
        """
        Gets the mediaLibrary property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._media_library
    
    @media_library.setter
    def media_library(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the mediaLibrary property value. Possible values of a property
        Args:
            value: Value to set for the mediaLibrary property.
        """
        self._media_library = value
    
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
    
    @property
    def photos(self,) -> Optional[enablement.Enablement]:
        """
        Gets the photos property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._photos
    
    @photos.setter
    def photos(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the photos property value. Possible values of a property
        Args:
            value: Value to set for the photos property.
        """
        self._photos = value
    
    @property
    def post_event(self,) -> Optional[enablement.Enablement]:
        """
        Gets the postEvent property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._post_event
    
    @post_event.setter
    def post_event(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the postEvent property value. Possible values of a property
        Args:
            value: Value to set for the postEvent property.
        """
        self._post_event = value
    
    @property
    def reminders(self,) -> Optional[enablement.Enablement]:
        """
        Gets the reminders property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._reminders
    
    @reminders.setter
    def reminders(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the reminders property value. Possible values of a property
        Args:
            value: Value to set for the reminders property.
        """
        self._reminders = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("accessibility", self.accessibility)
        writer.write_enum_value("addressBook", self.address_book)
        writer.write_collection_of_object_values("appleEventsAllowedReceivers", self.apple_events_allowed_receivers)
        writer.write_bool_value("blockCamera", self.block_camera)
        writer.write_bool_value("blockListenEvent", self.block_listen_event)
        writer.write_bool_value("blockMicrophone", self.block_microphone)
        writer.write_bool_value("blockScreenCapture", self.block_screen_capture)
        writer.write_enum_value("calendar", self.calendar)
        writer.write_str_value("codeRequirement", self.code_requirement)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("fileProviderPresence", self.file_provider_presence)
        writer.write_str_value("identifier", self.identifier)
        writer.write_enum_value("identifierType", self.identifier_type)
        writer.write_enum_value("mediaLibrary", self.media_library)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("photos", self.photos)
        writer.write_enum_value("postEvent", self.post_event)
        writer.write_enum_value("reminders", self.reminders)
        writer.write_enum_value("speechRecognition", self.speech_recognition)
        writer.write_bool_value("staticCodeValidation", self.static_code_validation)
        writer.write_enum_value("systemPolicyAllFiles", self.system_policy_all_files)
        writer.write_enum_value("systemPolicyDesktopFolder", self.system_policy_desktop_folder)
        writer.write_enum_value("systemPolicyDocumentsFolder", self.system_policy_documents_folder)
        writer.write_enum_value("systemPolicyDownloadsFolder", self.system_policy_downloads_folder)
        writer.write_enum_value("systemPolicyNetworkVolumes", self.system_policy_network_volumes)
        writer.write_enum_value("systemPolicyRemovableVolumes", self.system_policy_removable_volumes)
        writer.write_enum_value("systemPolicySystemAdminFiles", self.system_policy_system_admin_files)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def speech_recognition(self,) -> Optional[enablement.Enablement]:
        """
        Gets the speechRecognition property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._speech_recognition
    
    @speech_recognition.setter
    def speech_recognition(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the speechRecognition property value. Possible values of a property
        Args:
            value: Value to set for the speechRecognition property.
        """
        self._speech_recognition = value
    
    @property
    def static_code_validation(self,) -> Optional[bool]:
        """
        Gets the staticCodeValidation property value. Statically validates the code requirement. Use this setting if the process invalidates its dynamic code signature.
        Returns: Optional[bool]
        """
        return self._static_code_validation
    
    @static_code_validation.setter
    def static_code_validation(self,value: Optional[bool] = None) -> None:
        """
        Sets the staticCodeValidation property value. Statically validates the code requirement. Use this setting if the process invalidates its dynamic code signature.
        Args:
            value: Value to set for the staticCodeValidation property.
        """
        self._static_code_validation = value
    
    @property
    def system_policy_all_files(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicyAllFiles property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_all_files
    
    @system_policy_all_files.setter
    def system_policy_all_files(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicyAllFiles property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicyAllFiles property.
        """
        self._system_policy_all_files = value
    
    @property
    def system_policy_desktop_folder(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicyDesktopFolder property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_desktop_folder
    
    @system_policy_desktop_folder.setter
    def system_policy_desktop_folder(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicyDesktopFolder property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicyDesktopFolder property.
        """
        self._system_policy_desktop_folder = value
    
    @property
    def system_policy_documents_folder(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicyDocumentsFolder property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_documents_folder
    
    @system_policy_documents_folder.setter
    def system_policy_documents_folder(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicyDocumentsFolder property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicyDocumentsFolder property.
        """
        self._system_policy_documents_folder = value
    
    @property
    def system_policy_downloads_folder(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicyDownloadsFolder property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_downloads_folder
    
    @system_policy_downloads_folder.setter
    def system_policy_downloads_folder(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicyDownloadsFolder property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicyDownloadsFolder property.
        """
        self._system_policy_downloads_folder = value
    
    @property
    def system_policy_network_volumes(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicyNetworkVolumes property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_network_volumes
    
    @system_policy_network_volumes.setter
    def system_policy_network_volumes(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicyNetworkVolumes property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicyNetworkVolumes property.
        """
        self._system_policy_network_volumes = value
    
    @property
    def system_policy_removable_volumes(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicyRemovableVolumes property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_removable_volumes
    
    @system_policy_removable_volumes.setter
    def system_policy_removable_volumes(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicyRemovableVolumes property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicyRemovableVolumes property.
        """
        self._system_policy_removable_volumes = value
    
    @property
    def system_policy_system_admin_files(self,) -> Optional[enablement.Enablement]:
        """
        Gets the systemPolicySystemAdminFiles property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._system_policy_system_admin_files
    
    @system_policy_system_admin_files.setter
    def system_policy_system_admin_files(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the systemPolicySystemAdminFiles property value. Possible values of a property
        Args:
            value: Value to set for the systemPolicySystemAdminFiles property.
        """
        self._system_policy_system_admin_files = value
    

